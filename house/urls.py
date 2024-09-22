"""
URL configuration for rezerwacja_domkow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from house.views import HouseDetailView, HouseListView, create_reservation

urlpatterns = [
    path('', HouseListView.as_view(), name="house-list"),
    path("<int:pk>/", HouseDetailView.as_view(), name="house-detail"),
    path("<int:pk>/reserve", create_reservation, name="house-reserve"),
]
