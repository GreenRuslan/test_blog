from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def error(request):
    return render(request, 'accounts/error.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=user_name).exists() or \
                    User.objects.filter(email=email).exists():
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name,
                                                email=email,
                                                password=password,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save()
                return redirect('login')
        else:
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']

        user = auth.authenticate(username=user_name, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('blog_list')
        else:
            return redirect('error')
    return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
