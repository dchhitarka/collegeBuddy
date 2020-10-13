from django.shortcuts import render, redirect, reverse
# from django.http import HttpResponseRedirect, HttpResponse
# from student.models import Posts, Topics, Categories
# from django.contrib.auth.decorators import login_required
# from django.core.paginator import Paginator

def market(request):
    images = ['one', 'two', 'three', 'four', 'five']
    return render(request, 'market/market.html', {'images': images})
