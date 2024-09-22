from django.db import models

from managment.models import User
from django.db.models import Q
from django.utils.timezone import now

# Create your models here.

class House(models.Model):
    title = models.CharField(verbose_name="Nazwa domku", max_length=32)
    # picture = models.ImageField(verbose_name="Zdjecie domku")
    # localization = models.

    def __str__(self):
        return f"Domek {self.title} id: {self.id}"

    @property
    def is_reserved(self):
        return self.is_selected_days_reserved(now(), now())

    # lt - less than <
    # lte - less than equal <=
    # gt - greater than >
    # gte - greater than equal >=

    # | OR
    # & AND
    def is_selected_days_reserved(self, new_start_date, new_end_date):
        first_check = Q(
            reservations__start_date__lt=new_start_date,
            reservations__end_date__gt=new_start_date,
        )
        second_check = Q(
            reservations__start_date__gte=new_start_date,
            reservations__end_date__lte=new_end_date,
        )
        third_check = Q(
            reservations__start_date__lt=new_end_date,
            reservations__end_date__gt=new_end_date,
        )
        check = first_check | second_check | third_check
        return House.objects.filter(check, id=self.id).exists()


class Reservation(models.Model):
    house = models.ForeignKey(House, on_delete=models.PROTECT, related_name="reservations")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name="Poczatek rezerwacji")
    end_date = models.DateField(verbose_name="Koniec rezerwacji")

    def __str__(self):
        return f"Rezerwacja {self.id} domek {self.house}"