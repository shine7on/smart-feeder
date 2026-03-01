from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
from django.utils import timezone
from django.contrib import messages

from .scheduleForm import ScheduleForm
from .models import FeedingTime

# Create your views here.
def hello_world(request):
    return HttpResponse("hello world")

# how to accept request: UNUSE
def set_example(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        
        if form.is_valid():
            print("here")
            datetime = form.cleaned_data["datetime"]
        
        return render(request, "feeder/confirm.html", datetime)
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
    

# how to submit/receive request in one func w/ models
def feeding_view(request):
    if request.method == "POST":
        form = ScheduleForm(request.POST)

        if form.is_valid():
            saved = form.save()
            messages.success(
                request,
                f"Scheduled {timezone.localtime(saved.datetime).strftime('%Y-%m-%d %H:%M')}"
            )
            return redirect("feeding_view")  # redirect to GET
    else:
        form = ScheduleForm()
        times = FeedingTime.objects.all().order_by('datetime')
        print(times)
        # Get the system's local timezone
        now_local = timezone.localtime(timezone.now())
        current = now_local.strftime("%Y-%m-%dT%H:%M")
        return render(request, "feeder/main.html", {'form': form, 'times': times, 'current': current})