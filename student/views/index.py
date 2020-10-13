from django.shortcuts import render, redirect, reverse
# from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from student.models import Tasks, Notes, Timetable, Topics
import json

def index(request):
    if request.user.is_anonymous is False:
        return redirect('home')
    return render(request, 'index.html')

@login_required(login_url='login')
def home(request):
    tasks = Tasks.objects.filter(user=request.user).order_by('-created_on')[:3]
    notes = Notes.objects.filter(notes_by=request.user).order_by('-created_on')[:3]
    timetable = Timetable.objects.filter(user=request.user)
    if timetable: timetable = timetable[0]
    topics = Topics.objects.all().order_by('-topic_date')[:3]

    for task in tasks:
        task.tasks = json.loads(task.tasks)

    context = {
        'timetable': timetable, 
        'notes': notes, 
        'topics': topics, 
        'tasks': tasks
    }
    return render(request, 'home.html', context)
