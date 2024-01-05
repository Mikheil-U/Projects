from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task


class TaskList(ListView):
    # This will look for modelname_list.html so make sure to define one
    model = Task
    template_name = 'base/task_list.html'  # optional, but I still like to include it
