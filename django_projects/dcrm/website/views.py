from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
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


def delete_record(request, pk: int):
    if request.user.is_authenticated:
        del_record = Record.objects.get(id=pk)
        del_record.delete()
        messages.success(request, 'Record has successfully been deleted.')
        return redirect('home')
    else:
        messages.success(request, 'You must be logged in to do that.')
        return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                new_record = form.save()
                messages.success(request, "Record Added...")
                return redirect('home')
            else:
                messages.success(request, 'The form is invalid, please make sure to input the correct data.')
        return render(request, 'website/add_record.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in to do that.')
        return redirect('home')


def update_record(request, pk: int):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        # We use instance=current_record to keep the original data and keep the fields occupied with the original data,
        # So user don't need to re-enter all the information when they're only updating one field.
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated.")
            return redirect('home')
        return render(request, 'website/update_record.html', {'form': form})
    else:
        messages.success(request, 'The form is invalid, please make sure to input the correct data.')




