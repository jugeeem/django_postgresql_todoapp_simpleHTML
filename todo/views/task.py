from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView)
from ..models import *


class ToDoListView(ListView):
    """Show tasklist"""
    model = Task
    template_name = 'todo/todolist.html'
    context_object_name = 'task_list'


def add_task(request):
    """Add task
    
    Arguments:
        request {object} -- wsgi request object

    Returns:
        object -- wsgi response object
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasklist')
    else:
        form = TaskForm()
    return render(request, 'todo/add_task.html', {'form': form})