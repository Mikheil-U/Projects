from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from . models import Record


def home(request):
    # display the records
    records = Record.objects.all()

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
    else:  # They're logged in display the Records
        return render(request, 'website/home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')


def register_user(request):
    # Check to see if logging in
    if request.method == "POST":
        form = SignUpForm(request.POST)  # Get the data from the form
        if form.is_valid():
            form.save()
            # Authenticate and login the new user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully registered, Welcome!')
            return redirect('home')
    else:  # Create a form to be filled in
        form = SignUpForm()
    return render(request, 'website/register.html', {'form': form})


def customer_record(request, pk: int):
    if request.user.is_authenticated:  # if logged in
        # get the record
        cust_record = Record.objects.get(id=pk)
        return render(request, 'website/record.html', {'cust_record': cust_record})
    else:
        messages.success(request, 'You must be logged in to view that page...')
        return redirect('home')









