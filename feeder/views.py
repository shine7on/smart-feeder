from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from .scheduleForm import ScheduleForm

# Create your views here.
def hello_world(request):
    return HttpResponse("hello world")

# how to accept request
def set_example(request):
    if request.method == POST:
        time = request.POST.get('time')
    else:
        return HttpResponseNotAllowed('POST')

    return HttpResponse(f"You posted: {time}")

'''
def set_time (request):
    form = ScheduleForm(request.POST)

    if form.is_valid():
'''