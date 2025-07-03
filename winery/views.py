import requests
from django.shortcuts import render
CVINO_API = "https://fast-cvino-399730216663.europe-west1.run.app"

def home(request):
    return render(request, "winery/home.html")

def recommend(request):
    if request.method == "POST":
        # Build payload with proper data types and validation
        payload = {}

        # Handle grape varieties (multiple selection)
        grape_varieties = request.POST.getlist('grape_varieties')
        if grape_varieties and any(grape_varieties):  # Check if any non-empty values
            # Filter out empty strings
            filtered_grapes = [grape.strip() for grape in grape_varieties if grape.strip()]
            if filtered_grapes:
                payload['grape_varieties'] = filtered_grapes

        # Handle other fields
        for k, v in request.POST.items():
            if k in ['csrfmiddlewaretoken', 'grape_varieties']:
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

        # Country-Region validation mapping
        country_region_map = {
            'France': ['Bordeaux', 'Burgundy', 'Champagne', 'Loire Valley', 'Rhône Valley', 'Alsace', 'Languedoc'],
            'Italy': ['Tuscany', 'Piedmont', 'Veneto', 'Sicily', 'Umbria'],
            'Spain': ['Rioja', 'Ribera del Duero', 'Priorat', 'Rías Baixas'],
            'United States': ['Napa Valley', 'Sonoma County', 'Oregon', 'Washington'],
            'Australia': ['Barossa Valley', 'Hunter Valley', 'Margaret River'],
            'Argentina': ['Mendoza', 'Salta'],
            'Chile': ['Central Valley', 'Casablanca Valley']
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

            return render(request, "winery/recommend.html", {"wines": wines})
        except requests.exceptions.RequestException as e:
            return render(request, "winery/recommend_form.html", {"error": f"API Error: {str(e)}"})
    return render(request, "winery/recommend_form.html")

def pairing(request):
    if request.method == "POST":
        try:
            payload = {k: v for k, v in request.POST.items() if k != 'csrfmiddlewaretoken' and v}
            resp = requests.post(f"{CVINO_API}/recommend-by-food", json=payload, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            wines = data.get('wines', data) if isinstance(data, dict) else data
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
                'recommendations': data.get('recommendations', [])
            }

            # Process grape varieties if it's a list
            if isinstance(extracted_info['grape_varieties'], list):
                extracted_info['grape_varieties'] = ', '.join(extracted_info['grape_varieties'])

            return render(request, "winery/scan_result.html", extracted_info)
        except requests.exceptions.RequestException as e:
            return render(request, "winery/scanner_form.html", {"error": f"API Error: {str(e)}"})
    return render(request, "winery/scanner_form.html")
