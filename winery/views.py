import requests
from django.shortcuts import render
import csv
CVINO_API = "https://fast-cvino-399730216663.europe-west1.run.app"

def home(request):
    # Count unique regions and grapes for display on the home page
    region_count = 0
    country_count = 0
    with open('notebooks/unique_regions.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        regions = list(reader)
        region_count = len(regions)
        country_count = len(set(country for _, country in regions))

    grape_count = 0
    with open('notebooks/unique_grapes.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        grape_count = len(list(reader))

    context = {
        'region_count': region_count,
        'country_count': country_count,
        'grape_count': grape_count
    }
    return render(request, "winery/home.html", context)

def recommend(request):
    # Load data for the form from CSV files - do this for both GET and POST requests
    countries = []
    regions_data = {}
    with open('notebooks/unique_regions.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            region, country = row
            if country not in countries:
                countries.append(country)
            if country not in regions_data:
                regions_data[country] = []
            regions_data[country].append(region)

    # Sort regions within each country
    for country in regions_data:
        regions_data[country].sort()

    grapes = []
    with open('notebooks/unique_grapes.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # Skip header
        for row in reader:
            grapes.append(row[0].strip("[]'"))

    if request.method == "POST":
        # Build payload with proper data types and validation
        payload = {}

        # Handle grape varieties (multiple selection)
        grape_varieties = request.POST.getlist('grape_varieties[]')
        if not grape_varieties:  # Fall back to the old name if the new format isn't found
            grape_varieties = request.POST.getlist('grape_varieties')

        if grape_varieties and any(grape_varieties):  # Check if any non-empty values
            # Filter out empty strings
            filtered_grapes = [grape.strip() for grape in grape_varieties if grape.strip()]
            if filtered_grapes:
                payload['grape_varieties'] = filtered_grapes

        # Handle other fields
        for k, v in request.POST.items():
            if k in ['csrfmiddlewaretoken', 'grape_varieties', 'grape_varieties[]']:
                continue

            if v and v.strip():  # Only include non-empty, non-whitespace values
                if k == 'abv':
                    try:
                        payload[k] = float(v)
                    except (ValueError, TypeError):
                        continue  # Skip invalid ABV values
                elif k == 'n_recommendations':
                    try:
                        payload[k] = int(v)
                    except (ValueError, TypeError):
                        payload[k] = 5  # Default value
                else:
                    payload[k] = v.strip()

        # Country-Region validation mapping (comprehensive)
        country_region_map = {
            'France': [
                'Bordeaux', 'Burgundy', 'Champagne', 'Loire Valley', 'Rhône Valley', 'Alsace', 'Languedoc',
                'Terrasses du Larzac', 'Provence', 'Côtes du Rhône', 'Beaujolais', 'Jura', 'Savoie',
                'Corsica', 'Sud-Ouest', 'Bergerac', 'Cahors', 'Madiran', 'Jurançon', 'Gaillac',
                'Côtes de Gascogne', 'Côtes du Roussillon', 'Banyuls', 'Collioure', 'Fitou',
                'Corbières', 'Minervois', 'Saint-Chinian', 'Faugères', 'Pic Saint-Loup',
                'Coteaux du Languedoc', 'Muscadet', 'Sancerre', 'Pouilly-Fumé', 'Chablis',
                'Côte de Beaune', 'Côte de Nuits', 'Mâcon', 'Mercurey', 'Givry', 'Rully',
                'Châteauneuf-du-Pape', 'Hermitage', 'Côte-Rôtie', 'Condrieu', 'Saint-Joseph',
                'Crozes-Hermitage', 'Gigondas', 'Vacqueyras', 'Tavel', 'Lirac'
            ],
            'Italy': [
                'Tuscany', 'Piedmont', 'Veneto', 'Sicily', 'Umbria', 'Marche', 'Abruzzo',
                'Campania', 'Puglia', 'Calabria', 'Basilicata', 'Sardinia', 'Lombardy',
                'Trentino-Alto Adige', 'Friuli-Venezia Giulia', 'Emilia-Romagna', 'Lazio',
                'Molise', 'Valle d\'Aosta', 'Liguria', 'Chianti', 'Chianti Classico',
                'Brunello di Montalcino', 'Vino Nobile di Montepulciano', 'Barolo', 'Barbaresco',
                'Amarone della Valpolicella', 'Soave', 'Prosecco', 'Franciacorta', 'Lambrusco',
                'Sangiovese di Romagna', 'Trebbiano d\'Abruzzo', 'Montepulciano d\'Abruzzo',
                'Nero d\'Avola', 'Etna', 'Marsala', 'Pantelleria'
            ],
            'Spain': [
                'Rioja', 'Ribera del Duero', 'Priorat', 'Rías Baixas', 'Rueda', 'Toro',
                'Bierzo', 'Jumilla', 'Yecla', 'Alicante', 'Valencia', 'Utiel-Requena',
                'La Mancha', 'Valdepeñas', 'Montilla-Moriles', 'Jerez', 'Manzanilla',
                'Málaga', 'Sierras de Málaga', 'Condado de Huelva', 'Penedès', 'Cava',
                'Costers del Segre', 'Conca de Barberà', 'Tarragona', 'Terra Alta',
                'Montsant', 'Empordà', 'Pla de Bages', 'Alella', 'Catalunya',
                'Navarra', 'Campo de Borja', 'Calatayud', 'Cariñena', 'Somontano',
                'Cigales', 'Arribes', 'Tierra de León', 'Tierra del Vino de Zamora'
            ],
            'United States': [
                'Napa Valley', 'Sonoma County', 'Oregon', 'Washington', 'California',
                'Paso Robles', 'Santa Barbara County', 'Central Coast', 'Monterey',
                'Santa Cruz Mountains', 'Livermore Valley', 'Lodi', 'Mendocino',
                'Lake County', 'Sierra Foothills', 'Temecula Valley', 'Finger Lakes',
                'Long Island', 'Hudson River Region', 'Willamette Valley', 'Umpqua Valley',
                'Rogue Valley', 'Columbia Valley', 'Yakima Valley', 'Walla Walla Valley',
                'Red Mountain', 'Horse Heaven Hills', 'Rattlesnake Hills', 'Wahluke Slope',
                'Texas Hill Country', 'Virginia', 'North Carolina', 'Michigan', 'New York'
            ],
            'Australia': [
                'Barossa Valley', 'Hunter Valley', 'Margaret River', 'McLaren Vale',
                'Adelaide Hills', 'Clare Valley', 'Eden Valley', 'Coonawarra',
                'Yarra Valley', 'Mornington Peninsula', 'Grampians', 'Heathcote',
                'King Valley', 'Beechworth', 'Rutherglen', 'Goulburn Valley',
                'Central Victoria', 'Geelong', 'Macedon Ranges', 'Sunbury',
                'Tasmania', 'Great Southern', 'Mount Barker', 'Frankland River',
                'Porongurup', 'Denmark', 'Albany', 'Pemberton', 'Blackwood Valley',
                'Geographe', 'Peel', 'Perth Hills', 'Swan District'
            ],
            'Argentina': [
                'Mendoza', 'Salta', 'San Juan', 'La Rioja', 'Catamarca', 'Tucumán',
                'Córdoba', 'Neuquén', 'Río Negro', 'Chubut', 'Buenos Aires',
                'Entre Ríos', 'Maipú', 'Luján de Cuyo', 'Uco Valley', 'Tupungato',
                'Tunuyán', 'San Carlos', 'Agrelo', 'Perdriel', 'Chacras de Coria',
                'Vistalba', 'Las Compuertas', 'Cafayate', 'Molinos', 'Cachi',
                'Angastaco', 'San Carlos (Salta)', 'Seclantas', 'La Poma'
            ],
            'Chile': [
                'Central Valley', 'Casablanca Valley', 'Maipo Valley', 'Rapel Valley',
                'Colchagua Valley', 'Cachapoal Valley', 'Curicó Valley', 'Maule Valley',
                'Aconcagua Valley', 'San Antonio Valley', 'Leyda Valley', 'Lo Abarca',
                'Rosario Valley', 'Limari Valley', 'Choapa Valley', 'Elqui Valley',
                'Huasco Valley', 'Copiapo Valley', 'Bio Bio Valley', 'Itata Valley',
                'Malleco Valley', 'Osorno Valley', 'Cauquenes', 'Loncomilla',
                'Claro Valley', 'Lontué Valley', 'Molina', 'Sagrada Familia'
            ],
            'Germany': [
                'Mosel', 'Rheingau', 'Rheinhessen', 'Pfalz', 'Baden', 'Württemberg',
                'Nahe', 'Mittelrhein', 'Ahr', 'Franken', 'Hessische Bergstraße',
                'Saale-Unstrut', 'Sachsen', 'Bernkastel', 'Piesport', 'Wehlen',
                'Graach', 'Zeltingen', 'Ürzig', 'Erden', 'Kröv', 'Traben-Trarbach'
            ],
            'Portugal': [
                'Douro', 'Vinho Verde', 'Dão', 'Bairrada', 'Alentejo', 'Lisboa',
                'Tejo', 'Península de Setúbal', 'Algarve', 'Trás-os-Montes',
                'Beira Interior', 'Távora-Varosa', 'Lafões', 'Bucelas', 'Colares',
                'Carcavelos', 'Óbidos', 'Lourinhã', 'Torres Vedras', 'Alenquer',
                'Arruda', 'Encostas d\'Aire', 'Palmela', 'Moscatel de Setúbal'
            ],
            'South Africa': [
                'Stellenbosch', 'Paarl', 'Franschhoek', 'Walker Bay', 'Constantia',
                'Swartland', 'Tulbagh', 'Wellington', 'Worcester', 'Robertson',
                'Klein Karoo', 'Olifants River', 'Breede River Valley', 'Coastal Region',
                'Cape South Coast', 'Overberg', 'Elgin', 'Bot River', 'Hermanus',
                'Hemel-en-Aarde Valley', 'Durbanville', 'Tygerberg', 'Philadelphia'
            ],
            'New Zealand': [
                'Marlborough', 'Central Otago', 'Hawke\'s Bay', 'Martinborough',
                'Nelson', 'Canterbury', 'Gisborne', 'Auckland', 'Northland',
                'Wairarapa', 'Waipara Valley', 'Waitaki Valley', 'Bannockburn',
                'Gibbston', 'Cromwell', 'Alexandra', 'Bendigo', 'Lowburn',
                'Wanaka', 'Queenstown', 'Te Kauwhata', 'Kumeu', 'Henderson'
            ],
            'Austria': [
                'Wachau', 'Kremstal', 'Kamptal', 'Weinviertel', 'Burgenland',
                'Steiermark', 'Wien', 'Carnuntum', 'Thermenregion', 'Wagram',
                'Traisental', 'Donauland', 'Neusiedlersee', 'Leithaberg',
                'Mittelburgenland', 'Eisenberg', 'Rosalia', 'Vulkanland Steiermark',
                'Südsteiermark', 'Weststeiermark', 'Ruster Ausbruch'
            ],
            'Greece': [
                'Santorini', 'Nemea', 'Naoussa', 'Mantinia', 'Patras', 'Cephalonia',
                'Zante', 'Rhodes', 'Crete', 'Paros', 'Lemnos', 'Samos', 'Muscat of Samos',
                'Rapsani', 'Slopes of Meliton', 'Goumenissa', 'Amynteo', 'Messenikola',
                'Anchialos', 'Robola of Cephalonia', 'Muscat of Rio Patras'
            ],
            'Hungary': [
                'Tokaj', 'Eger', 'Villány', 'Szekszárd', 'Badacsony', 'Balaton',
                'Sopron', 'Mór', 'Neszmély', 'Etyek-Buda', 'Mátra', 'Bükk',
                'Kunság', 'Hajós-Baja', 'Csongrád', 'Tolna', 'Pannonhalma',
                'Zala', 'Somló', 'Nagy-Somló', 'Balatonfüred-Csopak'
            ],
            'Romania': [
                'Cotnari', 'Murfatlar', 'Dealu Mare', 'Târnave', 'Drăgășani',
                'Odobești', 'Panciu', 'Huși', 'Bohotin', 'Iași', 'Nicorești',
                'Pietroasa', 'Ștefănești', 'Segarcea', 'Sâmburești', 'Miniș',
                'Recaș', 'Banat', 'Crișana', 'Maramureș', 'Oltenia', 'Muntenia'
            ],
            'Bulgaria': [
                'Thracian Valley', 'Danubian Plain', 'Black Sea Region', 'Struma Valley',
                'Rose Valley', 'Plovdiv', 'Pazardzhik', 'Stara Zagora', 'Haskovo',
                'Burgas', 'Varna', 'Shumen', 'Razgrad', 'Ruse', 'Pleven', 'Vratsa',
                'Montana', 'Vidin', 'Blagoevgrad', 'Kyustendil', 'Pernik', 'Sofia'
            ],
            'Croatia': [
                'Istria', 'Kvarner', 'Dalmatia', 'Croatian Uplands', 'Slavonia',
                'Međimurje', 'Zagorje', 'Moslavina', 'Pokuplje', 'Prigorje-Bilogora',
                'Plešivica', 'Kutjevo', 'Krndija', 'Baranja', 'Podunavlje',
                'Pelješac', 'Korčula', 'Vis', 'Hvar', 'Brač', 'Pag'
            ],
            'Slovenia': [
                'Primorska', 'Podravje', 'Posavje', 'Goriška Brda', 'Vipava Valley',
                'Karst', 'Istria', 'Ljutomer-Ormož', 'Maribor', 'Radgona-Kapela',
                'Štajerska', 'Prekmurje', 'Dolenjska', 'Bela Krajina', 'Bizeljsko-Sremič'
            ],
            'Brazil': [
                'Serra Gaúcha', 'Vale dos Vinhedos', 'Campanha', 'Serra do Sudeste',
                'Campos de Cima da Serra', 'Vale do São Francisco', 'Bahia', 'Pernambuco',
                'Minas Gerais', 'São Paulo', 'Santa Catarina', 'Paraná', 'Espírito Santo'
            ],
            'Uruguay': [
                'Montevideo', 'Canelones', 'Colonia', 'San José', 'Florida', 'Maldonado',
                'Paysandú', 'Salto', 'Rivera', 'Tacuarembó', 'Durazno', 'Soriano'
            ]
        }

        # Validate country-region matching
        if payload.get('country') and payload.get('region_name'):
            country = payload['country']
            region = payload['region_name']
            if country in country_region_map and region not in country_region_map[country]:
                return render(request, "winery/recommend_form.html", {
                    "error": f"The region '{region}' does not belong to '{country}'. Please select a matching region."
                })

        # Ensure we have at least some criteria for recommendation
        if not payload:
            return render(request, "winery/recommend_form.html", {
                "error": "Please select at least one wine characteristic for recommendations."
            })

        try:
            resp = requests.post(f"{CVINO_API}/recommend-wines", json=payload, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            wines = data.get('wines', [])

            # Process wine data for template
            for wine in wines:
                # Process Grapes_list
                if wine.get('Grapes_list'):
                    grapes_str = wine['Grapes_list']
                    if isinstance(grapes_str, str) and grapes_str.startswith('['):
                        # Remove brackets and quotes, then split
                        grapes_str = grapes_str.strip('[]').replace("'", "")
                        wine['grapes_display'] = grapes_str
                    else:
                        wine['grapes_display'] = grapes_str
                else:
                    wine['grapes_display'] = 'N/A'

                # Process Harmonize
                if wine.get('Harmonize'):
                    harmonize_str = wine['Harmonize']
                    if isinstance(harmonize_str, str) and harmonize_str.startswith('['):
                        # Remove brackets and quotes, then split
                        harmonize_str = harmonize_str.strip('[]').replace("'", "")
                        wine['harmonize_display'] = harmonize_str
                    else:
                        wine['harmonize_display'] = harmonize_str
                else:
                    wine['harmonize_display'] = 'N/A'

                # Ensure WineName is populated
                if not wine.get('WineName'):
                    wine['WineName'] = 'Unknown Wine'

            return render(request, "winery/recommend.html", {"wines": wines})
        except requests.exceptions.RequestException as e:
            return render(request, "winery/recommend_form.html", {"error": f"API Error: {str(e)}"})

    context = {
        'countries': sorted(countries),
        'regions_data': regions_data,
        'grapes': sorted(grapes)
    }
    return render(request, "winery/recommend_form.html", context)


def pairing(request):
    if request.method == "POST":
        try:
            # Build payload with proper data handling
            payload = {}
            for k, v in request.POST.items():
                if k == 'csrfmiddlewaretoken':
                    continue
                if v and v.strip():  # Only include non-empty values
                    payload[k] = v.strip()

            # Ensure we have at least food_pairing
            if not payload.get('food_pairing'):
                return render(request, "winery/pairing_form.html", {
                    "error": "Please select a food type for wine pairing recommendations."
                })

            resp = requests.post(f"{CVINO_API}/recommend-by-food", json=payload, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            wines = data.get('wines', data) if isinstance(data, dict) else data

            # Process wine data for food pairing results
            for wine in wines:
                # Ensure WineName is populated
                if not wine.get('WineName'):
                    wine['WineName'] = 'Unknown Wine'

                # Process grapes if needed
                if wine.get('Grapes_list'):
                    grapes_str = wine['Grapes_list']
                    if isinstance(grapes_str, str) and grapes_str.startswith('['):
                        # Remove brackets and quotes, then split
                        grapes_str = grapes_str.strip('[]').replace("'", "")
                        wine['grapes_display'] = grapes_str
                    else:
                        wine['grapes_display'] = grapes_str
                else:
                    wine['grapes_display'] = 'N/A'

            return render(request, "winery/pairing.html", {"wines": wines})
        except requests.exceptions.RequestException as e:
            return render(request, "winery/pairing_form.html", {"error": f"API Error: {str(e)}"})
    return render(request, "winery/pairing_form.html")

def scanner(request):
    if request.method == "POST" and request.FILES.get("label"):
        try:
            files = {"img": request.FILES["label"].file}
            resp = requests.post(f"{CVINO_API}/read_image", files=files, timeout=30)
            resp.raise_for_status()
            data = resp.json()

            # Get the recommendations
            recommendations = data.get('recommendations', [])

            # Process recommendations to ensure WineName and Winery are populated
            for wine in recommendations:
                if not wine.get('WineName'):
                    wine['WineName'] = 'Unknown Wine'

                # Process grapes if needed
                if wine.get('Grapes_list'):
                    grapes_str = wine['Grapes_list']
                    if isinstance(grapes_str, str) and grapes_str.startswith('['):
                        # Remove brackets and quotes, then split
                        grapes_str = grapes_str.strip('[]').replace("'", "")
                        wine['grapes_display'] = grapes_str
                    else:
                        wine['grapes_display'] = grapes_str
                else:
                    wine['grapes_display'] = 'N/A'

            # Process the extracted wine information for the form
            extracted_info = {
                'wine_type': data.get('wine_type', ''),
                'grape_varieties': data.get('grape_varieties', ''),
                'body': data.get('body', ''),
                'abv': data.get('ABV', ''),
                'acidity': data.get('acidity', ''),
                'country': data.get('country', ''),
                'region': data.get('region', ''),
                'extraction_successful': data.get('extraction_successful', False),
                'recommendations': recommendations
            }

            # Process grape varieties if it's a list
            if isinstance(extracted_info['grape_varieties'], list):
                extracted_info['grape_varieties'] = ', '.join(extracted_info['grape_varieties'])

            return render(request, "winery/scan_result.html", extracted_info)
        except requests.exceptions.RequestException as e:
            return render(request, "winery/scanner_form.html", {"error": f"API Error: {str(e)}"})
    return render(request, "winery/scanner_form.html")
