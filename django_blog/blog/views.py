from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Registration View
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after registration
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

# Login View (Using built-in form)
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to home after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout View (Using built-in logout function)
def user_logout(request):
    logout(request)
    return redirect('login')

# Profile View (Logged-in user profile)
@login_required
def profile(request):
    return render(request, 'profile.html')
