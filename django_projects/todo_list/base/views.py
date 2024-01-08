from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import logout


from .models import Task


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        # to redirect the user after they have logged in
        return reverse_lazy('tasks')


def logout_user(request):
    logout(request)
    return redirect('tasks')


class TaskList(LoginRequiredMixin, ListView):
    # This will look for modelname_list.html so make sure to define one
    model = Task
    template_name = 'base/task_list.html'  # optional, but I still like to include it
    context_object_name = 'tasks'  # object_list is the default name Django uses for ListView CBV

    def get_context_data(self, **kwargs):
        # User specific data. So the user only gets their data.
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    # DetailView simply returns detailed information about the item
    # Define modelname_detail.html so DetailView can render the HTML.
    # Or use any name for an HTML file, but override the default name by setting the template_name
    model = Task
    context_object_name = 'task'  # default name is object
    template_name = 'base/task.html'  # override the default name


class TaskCreate(LoginRequiredMixin, CreateView):
    # Default template name is: modelname_form.html, create an HTML file with this name or
    # any other name, but set template_name to the new HTML file name.
    model = Task
    fields = ['title', 'description', 'complete']  # for ModelForm to create a form
    success_url = reverse_lazy('tasks')  # redirects the user after they add a new task

    def form_valid(self, form):
        # Only logged in user can create todos on their own account.
        # Previously any user could add items in other users todos.
        # There was an option to choose the User when we were creating a new todos.
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
