from django import forms
from django.utils import timezone
from .models import FeedingTime


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = FeedingTime
        fields = ['datetime']
        now_local = timezone.localtime(timezone.now())
        current = now_local.strftime("%Y-%m-%dT%H:%M")
        widgets = {
            'datetime': forms.DateTimeInput(
                attrs={'type': 'datetime-local',},
                format="%Y-%m-%dT%H:%M",
            )
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set correct input format
        self.fields["datetime"].input_formats = ["%Y-%m-%dT%H:%M"]

        # Set dynamic min time
        current = timezone.localtime().strftime("%Y-%m-%dT%H:%M")
        self.fields["datetime"].widget.attrs["min"] = current