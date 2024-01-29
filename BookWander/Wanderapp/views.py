from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to your home page
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to your home page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('home')  # Redirect to your home page