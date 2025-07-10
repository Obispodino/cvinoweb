# 🍷 CvalVino - Wine Recommendation System

CvalVino is an elegant web-based wine recommendation system built with Django that helps users discover wines based on characteristics, food pairings, and label scanning. The application leverages AI and a rich database of wine information to provide personalized recommendations.

## 🌟 Features

### 1. Wine Recommendations by Characteristics
- Search for wines based on:
  - Wine type (red, white, rosé, sparkling)
  - Grape varieties (from an extensive database)
  - Body profile (light, medium, full)
  - ABV (alcohol by volume)
  - Acidity level
  - Country and region of origin
  - And more criteria

### 2. Food & Wine Pairing
- Get wine recommendations that perfectly complement your meal
- Supports various food categories including:
  - Beef, poultry, and pork dishes
  - Seafood and fish
  - Vegetarian options
  - Desserts
  - Cheese plates
  - And many more food types

### 3. Wine Label Scanner
- Upload a photo of any wine label
- AI-powered analysis extracts information from the label including:
  - Wine name and producer
  - Grape varieties
  - Region of origin
  - Vintage
  - Wine type and characteristics
- Receive recommendations for similar wines based on the scanned label

## 🛠️ Technical Details

### Architecture
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django 5.2.4
- **External API**: Integration with CVINO_API for wine analysis and recommendations
- **Database**: Leverages CSV data files for wine regions, countries, and grape varieties

### Dataset
The application uses a comprehensive wine dataset featuring:
- **Wine Regions**: Over multiple regions across wine-producing countries
- **Countries**: Major wine-producing countries around the world
- **Grape Varieties**: Extensive list of grape varieties used in wine production

### API Integration
The system communicates with an external API service (CVINO_API) for:
- Wine recommendations based on user-selected characteristics
- Food and wine pairing suggestions
- Wine label image analysis and information extraction

## 📱 Progressive Web App (PWA)
CvalVino is designed as a Progressive Web App, offering:
- Mobile-friendly responsive design
- Fast loading times and smooth transitions
- Cross-device compatibility

## 🔍 How It Works

### Wine Recommendation Flow
1. Users select desired wine characteristics through an intuitive form
2. The system processes these preferences
3. API requests are made to retrieve matching wine recommendations
4. Results are presented in an elegant, informative interface

### Wine Label Scanner Process
1. User uploads a photo of a wine label
2. The image is sent to the API for analysis
3. AI extracts relevant information from the label
4. The system returns the extracted data and similar wine recommendations

## 💻 Installation & Setup

### Requirements
```
asgiref==3.9.0
certifi==2025.6.15
charset-normalizer==3.4.2
Django==5.2.4
idna==3.10
pillow==11.3.0
requests==2.32.4
sqlparse==0.5.3
typing_extensions==4.14.0
urllib3==2.5.0
```

### Local Development
1. Clone the repository
   ```bash
   git clone https://github.com/Obispodino/cvinoweb.git
   cd cvinoweb
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations
   ```bash
   python manage.py migrate
   ```

5. Start the development server
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`

## 🌐 Deployment
The application can be deployed on various platforms including:
- Heroku
- AWS
- DigitalOcean
- PythonAnywhere

## 🔮 Future Enhancements
- User accounts and personalized recommendation history
- Social sharing capabilities
- Wine collection management
- Advanced filtering and sorting options
- Enhanced mobile experience
- Integration with wine purchasing platforms

## 📊 Statistics
The system currently includes:
- Multiple wine regions across different countries
- Various wine-producing countries in the database
- Extensive collection of grape varieties

## 🧩 Project Structure
```
cvinoweb/
├── config/               # Django project settings
├── winery/               # Main app directory
│   ├── migrations/       # Database migrations
│   ├── static/           # CSS and images
│   ├── templates/        # HTML templates
│   ├── admin.py          # Admin configuration
│   ├── models.py         # Data models
│   ├── views.py          # View controllers
│   └── urls.py           # URL routing
├── notebooks/            # Data files and Jupyter notebooks
│   ├── exploration.ipynb # Data exploration notebook
│   ├── unique_grapes.csv # Grape varieties data
│   └── unique_regions.csv # Wine regions data
└── manage.py             # Django management script
```

## 📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements
- Wine data sourced from comprehensive wine databases
- Built with Django web framework
- Powered by AI for image recognition and recommendations

---

*CvalVino - Your Elegant Wine Recommendation System* 🍇🍷
