from django import forms

class ScheduleForm(forms.Form):
    time = forms.TimeField(required=True, label="Scheduled Time")