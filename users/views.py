from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, f'Account successfully created for {username}!')
        return redirect('login')

    return render(request, 'register.html', {})