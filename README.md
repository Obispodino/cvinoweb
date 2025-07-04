# 🍇🍷 CvalVino - Wine Recommendation System 🍷🍇

[![Django](https://img.shields.io/badge/Django-4.2+-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Mobile Optimized](https://img.shields.io/badge/Mobile-Optimized-brightgreen.svg)](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**CvalVino** is an elegant, AI-powered wine recommendation system that helps users discover perfect wines through multiple intelligent approaches. Whether you're a wine enthusiast, sommelier, or casual drinker, CvalVino provides personalized recommendations tailored to your preferences.

## 🌟 Features

### 🍷 **Wine Recommendation by Characteristics**
- **Advanced Filtering**: Search by wine type, grape varieties, body, ABV, acidity, country, and region
- **500+ Wine Regions**: Comprehensive database covering 20 countries and 500+ wine regions
- **59 Grape Varieties**: Extensive selection of red and white grape varieties
- **Smart Validation**: Real-time country-region matching to ensure accurate selections

### 🍽️ **Food & Wine Pairing**
- **Expert Pairings**: Get wine recommendations that perfectly complement your meal
- **Wine Type Selection**: Choose preferred wine type (Red, White, Rosé, Sparkling, Dessert, Fortified)
- **Diverse Food Categories**: From beef and seafood to vegetarian and spicy dishes
- **Curated Recommendations**: AI-powered suggestions based on culinary expertise

### 📸 **Wine Label Scanner (AI-Powered)**
- **Image Recognition**: Upload photos of wine labels for instant analysis
- **Information Extraction**: Automatically extract wine type, grape varieties, region, ABV, and more
- **Similar Wine Recommendations**: Get suggestions for wines similar to your scanned bottle
- **Mobile Optimized**: Perfect for scanning labels while shopping or dining

### 🔍 **Comprehensive Wine Database**
- **Detailed Wine Information**: Complete profiles including winery, type, grapes, body, ABV, region, country, acidity, and ratings
- **Food Pairing Suggestions**: Each wine includes recommended food pairings
- **Similarity Scoring**: Advanced algorithms to find wines that match your preferences
- **Vivino Integration**: Direct links to find wines on Vivino marketplace

## 🚀 Technology Stack

### **Backend**
- **Django 4.2+**: Robust web framework for rapid development
- **Python 3.8+**: Modern Python with type hints and async support
- **RESTful API**: Clean API architecture for wine recommendations
- **Advanced Validation**: Server-side validation for data integrity

### **Frontend**
- **Responsive Design**: Mobile-first approach optimized for all devices
- **Progressive Web App (PWA)**: App-like experience on mobile devices
- **CSS Grid & Flexbox**: Modern layout techniques for optimal display
- **JavaScript ES6+**: Enhanced user interactions and form validation

### **AI & Machine Learning**
- **Wine Label Recognition**: Computer vision for label analysis
- **Recommendation Engine**: Sophisticated algorithms for wine matching
- **Natural Language Processing**: Text extraction from wine labels
- **Similarity Algorithms**: Advanced matching based on wine characteristics

### **Mobile Optimization**
- **iPhone Optimized**: Native iOS Safari optimizations
- **Android Optimized**: Chrome and Android WebView enhancements
- **Touch-Friendly**: 44px minimum touch targets for accessibility
- **Responsive Images**: Optimized image loading for mobile networks

## 📱 Mobile Experience

### **iPhone Optimization**
- **iOS Safari Compatibility**: Optimized for Safari's unique rendering
- **Touch Callout Disabled**: Clean touch interactions without system popups
- **Viewport Meta Tags**: Proper scaling and zoom behavior
- **Apple Web App Meta Tags**: Enhanced home screen installation

### **Android Optimization**
- **Chrome Optimizations**: Leverages Chrome's advanced features
- **Material Design Elements**: Familiar Android UI patterns
- **Hardware Acceleration**: Smooth animations and transitions
- **Custom Select Styling**: Consistent dropdown appearance

### **Cross-Platform Features**
- **Responsive Breakpoints**: Optimized layouts for all screen sizes
- **Touch Gestures**: Intuitive swipe and tap interactions
- **Loading States**: Clear feedback during API calls
- **Offline Capability**: Basic functionality without internet connection

## 🛠️ Installation & Setup

### **Prerequisites**
```bash
# Required software
Python 3.8+
Django 4.2+
Git
```

### **Quick Start**
```bash
# 1. Clone the repository
git clone https://github.com/yourusername/cvinoweb.git
cd cvinoweb

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Start development server
python manage.py runserver
```

### **Environment Configuration**
```bash
# Create .env file (optional)
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
```

### **Production Deployment**
```bash
# Collect static files
python manage.py collectstatic

# Set production environment variables
export DEBUG=False
export SECRET_KEY=your-production-secret-key
export ALLOWED_HOSTS=yourdomain.com

# Use production WSGI server
gunicorn config.wsgi:application
```

## 🎯 Usage Guide

### **Getting Wine Recommendations**

1. **By Characteristics**:
   - Navigate to "Wine by Characteristics"
   - Select desired wine type, grape varieties, body, etc.
   - Choose country and region (automatically filtered)
   - Specify number of recommendations (3-20)
   - Click "Get Wine Recommendations"

2. **By Food Pairing**:
   - Go to "Food & Wine Pairing"
   - Select your food type from the dropdown
   - Choose preferred wine type (optional)
   - Get perfectly matched wine recommendations

3. **By Wine Label**:
   - Use the "Wine Label Scanner" on the home page
   - Upload a clear photo of any wine label
   - Review extracted information
   - Get recommendations for similar wines

### **Mobile Usage Tips**
- **Portrait Mode**: Optimized for vertical phone usage
- **Touch Targets**: All buttons are finger-friendly (44px minimum)
- **Swipe Navigation**: Smooth scrolling between sections
- **Image Upload**: Use camera or photo library for label scanning

## 🌍 Supported Regions

### **Countries & Regions** (500+ total)
- **🇫🇷 France** (47 regions): Bordeaux, Burgundy, Champagne, Loire Valley, Rhône Valley, Alsace, Languedoc, Terrasses du Larzac, Provence, and more
- **🇮🇹 Italy** (37 regions): Tuscany, Piedmont, Veneto, Sicily, Chianti, Barolo, Prosecco, and more
- **🇪🇸 Spain** (38 regions): Rioja, Ribera del Duero, Priorat, Rías Baixas, Cava, and more
- **🇺🇸 United States** (35 regions): Napa Valley, Sonoma County, Oregon, Washington, Finger Lakes, and more
- **🇦🇺 Australia** (33 regions): Barossa Valley, Hunter Valley, Margaret River, and more
- **🇦🇷 Argentina** (29 regions): Mendoza, Salta, Uco Valley, and more
- **🇨🇱 Chile** (28 regions): Central Valley, Casablanca Valley, Maipo Valley, and more
- **🇩🇪 Germany** (22 regions): Mosel, Rheingau, Rheinhessen, Pfalz, and more
- **🇵🇹 Portugal** (24 regions): Douro, Vinho Verde, Dão, Alentejo, and more
- **🇿🇦 South Africa** (23 regions): Stellenbosch, Paarl, Franschhoek, and more
- **🇳🇿 New Zealand** (23 regions): Marlborough, Central Otago, Hawke's Bay, and more
- **Plus 9 more countries**: Austria, Greece, Hungary, Romania, Bulgaria, Croatia, Slovenia, Brazil, Uruguay

### **Grape Varieties** (59 total)
**Red Grapes**: Cabernet Sauvignon, Merlot, Pinot Noir, Syrah, Shiraz, Malbec, Tempranillo, Sangiovese, Grenache, Barbera, Nebbiolo, Zinfandel, and more

**White Grapes**: Chardonnay, Sauvignon Blanc, Riesling, Pinot Grigio, Pinot Gris, Gewürztraminer, Albariño, Viognier, Chenin Blanc, Moscato, and more

## 🔧 API Documentation

### **Wine Recommendation Endpoint**
```http
POST /recommend-wines/
Content-Type: application/json

{
  "wine_type": "Red",
  "grape_varieties": ["Cabernet Sauvignon", "Merlot"],
  "body": "Full-bodied",
  "abv": 14.5,
  "acidity": "Medium",
  "country": "France",
  "region_name": "Bordeaux",
  "n_recommendations": 5
}
```

### **Food Pairing Endpoint**
```http
POST /recommend-by-food/
Content-Type: application/json

{
  "food_pairing": "Beef",
  "wine_type": "Red"
}
```

### **Wine Label Scanner Endpoint**
```http
POST /read_image/
Content-Type: multipart/form-data

img: [image file]
n_recommendations: 5
```

## 🎨 Design Philosophy

### **User Experience**
- **Intuitive Navigation**: Clear, logical flow between features
- **Visual Hierarchy**: Important elements stand out with proper contrast
- **Consistent Branding**: Elegant wine-themed color palette throughout
- **Accessibility**: WCAG 2.1 compliant with keyboard navigation support

### **Mobile-First Design**
- **Progressive Enhancement**: Core functionality works on all devices
- **Touch-Optimized**: Gestures and interactions designed for mobile
- **Performance**: Optimized loading times and smooth animations
- **Offline Support**: Basic functionality available without internet

### **Color Palette**
- **Primary Burgundy** (#722F37): Main brand color, sophisticated and wine-themed
- **Secondary Pink** (#F4A6B1): Warm accent color for cards and highlights
- **Accent Red** (#c24f5d): Call-to-action buttons and interactive elements
- **Text Colors**: High contrast white and dark text for readability

## 🔒 Security Features

### **Data Protection**
- **CSRF Protection**: Django's built-in CSRF middleware
- **Input Validation**: Server-side validation for all user inputs
- **File Upload Security**: Restricted file types and size limits
- **SQL Injection Prevention**: Django ORM protects against SQL injection

### **Privacy**
- **No Personal Data Storage**: Only wine preferences are processed
- **Secure File Handling**: Uploaded images are processed securely
- **HTTPS Ready**: SSL/TLS encryption support for production
- **GDPR Compliant**: Minimal data collection and processing

## 🚀 Performance Optimizations

### **Frontend Performance**
- **CSS Optimization**: Minified stylesheets with efficient selectors
- **Image Optimization**: Responsive images with proper sizing
- **JavaScript Efficiency**: Modern ES6+ with minimal DOM manipulation
- **Caching Strategy**: Browser caching for static assets

### **Backend Performance**
- **Database Optimization**: Efficient queries with proper indexing
- **API Response Caching**: Reduced server load with smart caching
- **Asynchronous Processing**: Non-blocking operations for better UX
- **CDN Ready**: Static file serving optimization

## 🧪 Testing

### **Manual Testing Checklist**
- ✅ Wine recommendation by characteristics
- ✅ Food and wine pairing functionality
- ✅ Wine label scanner with image upload
- ✅ Country-region validation and filtering
- ✅ Mobile responsiveness on iOS and Android
- ✅ Form validation and error handling
- ✅ API error handling and user feedback

### **Browser Compatibility**
- ✅ **iOS Safari** (12+)
- ✅ **Chrome Mobile** (80+)
- ✅ **Firefox Mobile** (75+)
- ✅ **Samsung Internet** (10+)
- ✅ **Desktop Chrome** (80+)
- ✅ **Desktop Firefox** (75+)
- ✅ **Desktop Safari** (13+)

## 🤝 Contributing

We welcome contributions to CvalVino! Here's how you can help:

### **Development Setup**
```bash
# Fork the repository
git clone https://github.com/yourusername/cvinoweb.git

# Create feature branch
git checkout -b feature/your-feature-name

# Make changes and test
python manage.py test

# Submit pull request
git push origin feature/your-feature-name
```

### **Contribution Guidelines**
- Follow PEP 8 style guidelines for Python code
- Write descriptive commit messages
- Add tests for new functionality
- Update documentation for API changes
- Ensure mobile compatibility for UI changes

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Wine Data**: Based on comprehensive wine databases and expert knowledge
- **Design Inspiration**: Modern web design principles and wine industry aesthetics
- **AI Technology**: Advanced machine learning for wine recommendations
- **Community**: Thanks to all contributors and wine enthusiasts who provided feedback

## 📞 Support

### **Getting Help**
- **Documentation**: Check this README and inline code comments
- **Issues**: Report bugs via GitHub Issues
- **Feature Requests**: Submit enhancement ideas through GitHub
- **Community**: Join discussions in the project's GitHub Discussions

### **Contact Information**
- **Project Maintainer**: [Your Name]
- **Email**: [your.email@example.com]
- **GitHub**: [@yourusername](https://github.com/yourusername)
- **Website**: [https://cvalvino.example.com](https://cvalvino.example.com)

---

**Made with ❤️ for wine lovers everywhere**

*CvalVino - Where technology meets terroir*
