from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("recommend/", views.recommend, name="recommend"),
    path("pairing/", views.pairing, name="pairing"),
    path("scanner/", views.scanner, name="scanner"),
]
