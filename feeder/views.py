from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from .scheduleForm import ScheduleForm

# Create your views here.
def hello_world(request):
    return HttpResponse("hello world")

# how to accept request
def set_example(request):
    if request.method == 'POST':
        time = request.POST.get('datetime')

        return HttpResponse(f"You posted: {time}")
    else:
        return HttpResponseNotAllowed('POST')

# how to submit the request (form)
def submit_example(request):
    return render(request, "feeder/submit.html")

# how to show the confirm message
def confirm_example(request):
    if request.method == 'POST':
        time = {"time": request.POST.get('datetime')}
        return render(request, "feeder/confirm.html", time)


'''
def set_time (request):
    form = ScheduleForm(request.POST)

    if form.is_valid():
'''