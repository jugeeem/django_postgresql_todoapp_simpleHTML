import logging

from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView)
# login必須の関数viewにはこれを必ず一番先頭に継承する
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# login必須のClassViewにはこれを必ず一番先頭に継承する
from django.contrib.auth.decorators import login_required

from ..models import *


logger = logging.getLogger(__name__)


class ToDoListView(LoginRequiredMixin, ListView):
    """Show tasklist"""
    model = Task
    template_name = 'todo/show_tasklist.html'
    context_object_name = 'task_list'
    queryset = Task.objects.filter(delete_flag=False).order_by('-created_at')


class DirectorListView(LoginRequiredMixin, ListView):
    """Show directorlist"""
    model = Director
    template_name = 'todo/show_directorlist.html'
    context_object_name = 'director_list'
    queryset = Director.objects.filter(
        delete_flag=False).order_by('-created_at')


class TaskDetailView(LoginRequiredMixin, DetailView):
    """Show task detail"""
    model = Task
    template_name = "todo/show_taskdetail.html"
    context_object_name = 'task'


class TaskCreateView(LoginRequiredMixin, CreateView):
    """Create task"""
    model = Task
    template_name = 'todo/add_task.html'
    fields = [
        'director',
        'title',
        'description',
        'status'
    ]
    success_url = reverse_lazy('show_tasklist')


class DirectorCreateView(LoginRequiredMixin, CreateView):
    """Create director"""
    model = Director
    template_name = 'todo/add_director.html'
    fields = ['title']
    success_url = reverse_lazy('show_directorlist')


class UpdateTaskView(LoginRequiredMixin, UpdateView):
    """Update task"""
    model = Task
    template_name = 'todo/update_task.html'
    fields = [
        'title',
        'description',
        'director',
        'status'
    ]
    success_url = reverse_lazy('show_tasklist')


class UpdateDirectorView(LoginRequiredMixin, UpdateView):
    """Update director"""
    model = Director
    template_name = 'todo/update_director.html'
    fields = ['title']
    success_url = reverse_lazy('show_directorlist')


class DeleteTaskView(LoginRequiredMixin, UpdateView):
    """SoftDelete task"""
    model = Task
    template_name = 'todo/delete_task.html'
    fields = ['delete_flag']
    success_url = reverse_lazy('show_tasklist')


class DeleteDirectorView(LoginRequiredMixin, UpdateView):
    """SoftDelete director"""
    model = Director
    template_name = 'todo/delete_director.html'
    fields = ['delete_flag']
    success_url = reverse_lazy('show_tasklist')
