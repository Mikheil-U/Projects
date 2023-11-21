from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .models import Movie


def index(request):

    return render(request, 'movies_app/base.html', {'movies': Movie.objects.all()})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    if request.method == "POST":
        pass


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


