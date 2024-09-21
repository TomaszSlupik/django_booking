from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from house.models import House

# Create your views here.

class HouseListView(ListView):
    model = House
    template_name = "house_list.html"


class HouseDetailView(DetailView):
    model = House
    template_name = "house_detail.html"


