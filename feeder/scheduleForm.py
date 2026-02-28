from django import forms

class ScheduleForm(forms.Form):
    time = forms.DateTimeField(required=True, label="Scheduled Time")