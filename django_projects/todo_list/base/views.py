from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task


class TaskList(ListView):
    # This will look for modelname_list.html so make sure to define one
    model = Task
    template_name = 'base/task_list.html'  # optional, but I still like to include it
    context_object_name = 'tasks'  # object_list is the default name Django uses for ListView CBV


class TaskDetail(DetailView):
    # DetailView simply returns detailed information about the item
    # Define modelname_detail.html so DetailView can render the HTML.
    # Or use any name for an HTML file, but override the default name by setting the template_name
    model = Task
    context_object_name = 'task'  # default name is object
    template_name = 'base/task.html'  # override the default name
