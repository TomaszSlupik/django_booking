from django.contrib import admin
from django.urls import include, path

from house.views import HouseListView, HouseDetailView

urlpatterns = [
    path('', HouseListView.as_view(), name="house_list"),
     path('<int:pk>/', HouseDetailView.as_view(), name='house_detail'),
]
