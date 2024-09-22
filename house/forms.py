from django.forms import ModelForm, ValidationError, widgets
from django.utils.timezone import now
from datetime import date
from house.models import Reservation


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ["start_date", "end_date"]
        widgets = {
            'start_date': widgets.DateInput(attrs={'type': 'date'}),
            'end_date': widgets.DateInput(attrs={'type': 'date'})
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        date_now = now()
        today = date(date_now.year, date_now.month, date_now.day)
        if start_date < today or end_date < today:
            raise ValidationError(
                "Start_date and End_date cannot be from the past"
            )
            