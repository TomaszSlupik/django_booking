from django.db import models
from managment.models import User


class House(models.Model):
    title = models.CharField(verbose_name="Nazwa domu", max_length=100) 
    # picture = models.ImageField(verbose_name="Zdjecie domku")
    # localization = models.

    def __str__(self):
        return f"Domek {self.title} id: {self.id}"


class Reservation(models.Model):
    house = models.ForeignKey(House, on_delete=models.PROTECT, related_name="reservations")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name="Poczatek rezerwacji")
    end_date = models.DateField(verbose_name="Koniec rezerwacji")

    def __str__(self):
        return f"Rezerwacja {self.id} domek {self.house}"