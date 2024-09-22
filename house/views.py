from typing import Any
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.timezone import now

from house.forms import ReservationForm
from house.models import House, Reservation
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# Create your views here.

class HouseListView(ListView):
    model = House
    template_name = "house_list.html"

    def get_queryset(self):
        qs = House.objects.filter(reservations__isnull=True)
        return qs
    
        

class HouseDetailView(DetailView):
    model = House
    template_name = "house_detail.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["form"] = ReservationForm()
        return context

@csrf_protect
def create_reservation(request, pk):
    if request.method == "POST" and request.user.is_authenticated:
        form = ReservationForm(request.POST)
        house = get_object_or_404(House, pk=pk)
        if form.is_valid():
            start_date = form.cleaned_data["start_date"]
            end_date = form.cleaned_data["end_date"]
            if start_date > end_date:
                start_date, end_date = end_date, start_date
            if not house.is_selected_days_reserved(start_date, end_date):
                Reservation.objects.create(
                    house=house,
                    user=request.user,
                    start_date = start_date,
                    end_date=end_date,
                )
                # TODO redirect do profilu
        else:
            return render(request, "house_detail.html", {"object": house, "form":form})
    return redirect("house-list")





  