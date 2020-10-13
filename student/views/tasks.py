from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse
from student.models import Tasks
from django.contrib.auth.decorators import login_required
import json
@login_required(login_url='login')
def tasks(request):
    tasks = Tasks.objects.filter(user=request.user)
    for task in tasks:
        task.tasks = json.loads(task.tasks)
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
    print(task)
    return render(request, 'tasks/editTask.html', {'task': task})   

@login_required(login_url='login')
def deleteTask(request, pk):
    task = Tasks.objects.get(pk=pk)
    task.delete()
    return redirect('tasks')    
