from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from datetime import datetime

from .scheduleForm import ScheduleForm

# Create your views here.
def hello_world(request):
    return HttpResponse("hello world")

# how to accept request: UNUSE
def set_example(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        
        if form.is_valid():
            time = form.cleaned_data["datetime"]
        
        return render(request, "feeder/confirm.html", time)
    else:
        return HttpResponseNotAllowed('POST')

def submit_form_example(request):
    form = ScheduleForm()
    return render(request, "feeder/submit_form.html", {"form":form})

# how to submit the request (form)
def submit_example(request):
    today = datetime.now().strftime("%Y-%m-%dT%H:%M")
    return render(request, "feeder/submit.html", {'current': today})

# how to show the confirm message
def confirm_example(request):
    if request.method == 'POST':
        time = {"time": request.POST.get('datetime')}
        return render(request, "feeder/confirm.html", time)