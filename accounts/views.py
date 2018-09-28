from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objexts.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username is already exit.'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=[password1])
                auth.login(request,user)
                return redirect('home')
            else:
                return render(request, 'accounts/signup.html', {'error': 'Confirm password dose not match.'})
    else:
        return render(request, 'accounts/signup.html', {'error': 'Please input the information.'})

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    # TODO Need to rout to homepage
    # and dont forget to logout
    return render(request, 'accounts/signup.html')
