from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse
from student.models import UserAccount
from django.contrib import messages
from django.contrib.auth import authenticate, login
from student.authbackend import UserAccountBackend

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
        UserAccount.objects.create_user(username=username, email=email, reg_no=reg_no, password=password, first_name=first_name, last_name=last_name)
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
