from django.shortcuts import render
from django.http import HttpResponse

def attendance(request):
    return HttpResponse(content="<h1>This is Attendance View</h1>")