from django.shortcuts import render, redirect
from django.http import JsonResponse
from student.models import Timetable
from django.contrib.auth.decorators import login_required
import json, re

@login_required(login_url='login')
def timetable(request):
    timetable = Timetable.objects.filter(user=request.user)
    if not timetable:
        timetable = Timetable.objects.create(user=request.user)
        timetable.timetable = "[]"
    else:
        timetable = timetable[0]
        timetable.timetable = re.sub(r"None", 'null', timetable.timetable)
    print(timetable.timetable)
    return render(request, 'timetable/timetable.html', {"timetable": timetable})


@login_required(login_url='login')
def timetableSave(request):
    if request.method == "POST":
        try:
            newTimetable = json.loads(request.body)
            timetable = Timetable.objects.filter(user=request.user)
            if not timetable:
                timetable = Timetable.objects.create(user=request.user)
            else:
                timetable = timetable[0]
            timetable.timetable = newTimetable
            timetable.save()
            return JsonResponse(data = {"msg": "Timetable updated successfully"})
        except Exception as e:
            print(e)
            return JsonResponse(data = {"msg": "Some error occurred! Please try again."}, status=500)
    return redirect('timetable')

