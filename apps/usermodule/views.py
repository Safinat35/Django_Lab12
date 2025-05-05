from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please check the form.')
            return redirect('register')
    else:
        form = UserCreationForm()
    return render(request, 'usermodule/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('list_students') 
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request, 'usermodule/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'Logged out.')
    return redirect('login')
