from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse
from student.models import Notes
from student.forms import NotesForm
from django.contrib.auth.decorators import login_required

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
