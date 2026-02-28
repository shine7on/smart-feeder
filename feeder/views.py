from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from django.utils import timezone

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

# submit the form used  Django form: UNUSE
def submit_form_example(request):
    form = ScheduleForm()
    return render(request, "feeder/submit_form.html", {"form":form})


# how to submit the request (form)
def submit_example(request):
    # Get the system's local timezone
    now_local = timezone.localtime(timezone.now())
    current = now_local.strftime("%Y-%m-%dT%H:%M")
    return render(request, "feeder/submit.html", {'current': current})

# how to show the confirm message
def confirm_example(request):
    if request.method == 'POST':
        time = {"time": request.POST.get('datetime')}
        return render(request, "feeder/confirm.html", time)