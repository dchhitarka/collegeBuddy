from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from student.models import Timetable
from django.contrib.auth.decorators import login_required
import json

@login_required(login_url='login')
def timetable(request):
    timetable = Timetable.objects.filter(user=request.user)
    if timetable: timetable = timetable[0]
    return render(request, 'timetable/timetable.html', {"timetable": timetable})

@login_required(login_url='login')
def timetableSave(request):
    if request.method == "POST":
        try:
            newTimetable = json.loads(request.body)
            timetable = Timetable.objects.get(user=request.user)
            timetable.timetable = newTimetable
            timetable.save()
            return JsonResponse(data = {"msg": "Timetable updated successfully"})
        except:
            return JsonResponse(data = {"msg": "Some error occurred! Please try again."}, status=500)
    return redirect('timetable')

