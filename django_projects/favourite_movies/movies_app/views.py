from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .models import Movie


def index(request):

    return render(request, 'movies_app/base.html', {'movies': Movie.objects.all()})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to a success page.
            else:
                # Return an 'invalid login' error message.
                return render(request, 'movies_app/login.html', {'form': form, 'error': 'Invalid username or password.'})
    else:
        form = AuthenticationForm()

    return render(request, 'movies_app/login.html', {'form': form})


