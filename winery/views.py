import requests
from django.shortcuts import render
CVINO_API = "https://api.cvalvino.com"   # adapt if self-hosted

def home(request):
    return render(request, "winery/home.html")

def recommend(request):
    if request.method == "POST":
        payload = {k: v for k, v in request.POST.items() if v}
        resp = requests.post(f"{CVINO_API}/recommend-wines", json=payload, timeout=10)
        wines = resp.json()
        return render(request, "winery/recommend.html", {"wines": wines})
    return render(request, "winery/recommend_form.html")

def pairing(request):
    if request.method == "POST":
        payload = {k: v for k, v in request.POST.items() if v}
        resp = requests.post(f"{CVINO_API}/recommend-by-food", json=payload, timeout=10)
        wines = resp.json()
        return render(request, "winery/pairing.html", {"wines": wines})
    return render(request, "winery/pairing_form.html")

def scanner(request):
    if request.method == "POST" and request.FILES.get("label"):
        files = {"img": request.FILES["label"].file}
        resp = requests.post(f"{CVINO_API}/read_image", files=files, timeout=10)
        data = resp.json()
        return render(request, "winery/scan_result.html", data)
    return render(request, "winery/scanner_form.html")
