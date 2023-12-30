from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    # Check to see if logging in
    if request.method == "POST":
        username = request.POST['username']  # Grab username from HTML input field, we named it 'username'
        password = request.POST['password']  # Grab password from HTML input field, we named it 'password'

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            # Always add messages in HTML file, See base.html
            messages.error(request, "There was an error logging in, Please try again")
            return redirect('home')
    else:
        return render(request, 'website/home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')


def register_user(request):
    return render(request, 'website/register.html', {})
