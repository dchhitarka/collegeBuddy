from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *     
from .models import * 
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .authbackend import UserAccountBackend
from django.core.paginator import Paginator
from django.utils.html import format_html
import json
from django.contrib.auth.decorators import login_required

def index(request):
    if request.user.is_anonymous is False:
        return redirect('home')
    return render(request, 'index.html')

@login_required(login_url='login')
def home(request):
    tasks = Tasks.objects.filter(user=request.user).order_by('-created_on')[:3]
    notes = Notes.objects.filter(notes_by=request.user).order_by('-created_on')[:3]
    timetable = Timetable.objects.filter(user=request.user)
    if timetable:
        timetable = timetable[0]
    print(timetable)
    topics = Topics.objects.all().order_by('-topic_date')[:3]
    context = {
        'timetable': timetable, 
        'notes': notes, 
        'topics': topics, 
        'tasks': tasks
    }
    return render(request, 'home.html', context)
    
# Authentication Views
def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        reg_no = request.POST.get('reg_no')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_pw = request.POST.get('confirm_pw')
        if password and confirm_pw and password != confirm_pw:
            messages.error(request, "Password do not match!")
            return render(request, 'registration/register.html')
        newUser = UserAccount.objects.create_user(username=username, email=email, reg_no=reg_no, password=password, first_name=first_name, last_name=last_name)
        messages.success(request, 'Your account was successfully created. Login to use your account.')
        return HttpResponseRedirect('login')

    return render(request, 'registration/register.html')    

def loginView(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return redirect('/')
    return render(request, 'registration/login.html')

# Profile Views
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'profile/dashboard.html')

# Timetable Views
@login_required(login_url='login')
def timetable(request):
    return render(request, 'timetable/manage.html')

@login_required(login_url='login')
def timetableSave(request):
    print(request.user)
    newData = request.GET.get('data')
    timetable = Timetable.objects.get(user=request.user)
    timetable.timetable = newData
    timetable.save()
    return redirect('timetable');

# Attendance Views
@login_required(login_url='login')
def attendance(request):
    pass

# Tasks Views
@login_required(login_url='login')
def tasks(request):
    tasks = Tasks.objects.filter(user=request.user)
    return render(request, 'tasks/tasks.html', {'tasks': tasks})


@login_required(login_url='login')
def newTask(request):
    if request.method == 'POST':
        taskContent = request.POST['task']
        user = request.user
        task = Tasks.objects.create(tasks=taskContent, user=user)
        task.save()
        return redirect('tasks')
    return render(request, 'tasks/newTask.html')    

@login_required(login_url='login')
def editTask(request, pk):
    task = Tasks.objects.get(pk=pk)
    if request.method == 'POST':
        task.tasks = request.POST['task']
        task.color = request.POST['color']
        task.save()
        return redirect('tasks')
    return render(request, 'tasks/editTask.html', {'task': task})   

@login_required(login_url='login')
def deleteTask(request, pk):
    task = Tasks.objects.get(pk=pk)
    task.delete()
    return redirect('tasks')    

# Notes Views
@login_required(login_url='login')
def notes(request):
    notes = Notes.objects.filter(notes_by=request.user)
    return render(request, 'notes/notes.html', {'notes': notes})

@login_required(login_url='login')
def newNote(request):
    if request.method == 'POST':
        title   = request.POST['title']
        content = request.POST['content']
        color   = request.POST['color']
        user    = request.user
        note    = Notes.objects.create(title=title, content=content, notes_by=user, color=color)
        note.save()
        return redirect('notes')
    form = NotesForm()
    return render(request, 'notes/newNote.html', {'form': form}) 

@login_required(login_url='login')
def editNote(request, pk):
    note = Notes.objects.get(pk=pk)
    if request.method == 'POST':
        note.title   = request.POST['title']
        note.content = request.POST['content']
        note.color   = request.POST['color']
        note.save()
        return redirect('notes')
    content = note.content
    form = NotesForm(initial={'content': content})
    return render(request, 'notes/editNote.html', {'form': form, 'note': note}) 

@login_required(login_url='login')
def deleteNote(request, pk):
    note = Notes.objects.get(pk=pk)
    note.delete()
    return redirect('notes')

# Settings Views
@login_required(login_url='login')
def settings(request):
    return render(request, 'settings/settings.html')

# Community Views
def community(request):
    categories = Categories.objects.all()
    topics = Topics.objects.all().order_by('-topic_posts')
    posts = Posts.objects.all()
    return render(request, 'community/latest.html', {
                                                        'categories': categories,
                                                        'topics': topics,
                                                        'posts': posts
                                                    })

# This view is for topic.html page which shows a particular thread
def topic(request, pk):
    if request.method == 'POST' and request.user.is_anonymous == False:
        topic = Topics.objects.get(pk=pk)
        post_content = request.POST.get('content')
        post_by = request.user
        post_topic = topic
        post = Posts.objects.create(post_content=post_content, post_by=post_by, post_topic=post_topic)
        topic.topic_posts += 1
        topic.save()
        post.save()
        return redirect('showTopic', topic.pk)
    topic = Topics.objects.get(pk=pk)
    posts = Posts.objects.filter(post_topic=topic).order_by('-post_date')
    form = PostForm()
    return render(request, 'community/topic.html', {'topic': topic, 'posts': posts, 'form': form})

# This view is for forumList.html which shows all threads available
def topicList(request):
    forums_list = Topics.objects.all().order_by('-topic_date')
    page = request.GET.get('page')
    paginator = Paginator(forums_list, 7)
    forums = paginator.get_page(page)
    return render(request, 'community/forumList.html', {'forums': forums})


def createTopic(request):
    if request.method == 'POST':
        topic_content = request.POST.get('content')
        topic_by = request.user
        topic_name = request.POST.get('name')
        topic_cat = request.POST.get('cat')
        cat = Categories.objects.get(cat_name=topic_cat)
        topic = Topics.objects.create(topic_desc=topic_content, topic_by=topic_by, topic_name=topic_name, topic_cat=cat)
        cat.cat_topics += 1
        cat.save()
        topic.save()
        return redirect('threads')
    cats = Categories.objects.all()
    return render(request, 'community/createTopic.html', {'cats': cats})

def search(request):
    return HttpResponse("Hello Forum")

#  Forum Suggestions Views
def suggestions(request):
    return HttpResponse("Hello Forum")

# Forum Members Views
def members(request):
    return HttpResponse("Hello Forum")


# Market Views
def market(request):
    images = ['one', 'two', 'three', 'four', 'five']
    return render(request, 'market/market.html', {'images': images})
