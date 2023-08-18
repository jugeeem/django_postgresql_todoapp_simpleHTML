from django.urls import path
from . import views


urlpatterns = [
    # view for todolist
    path('', views.ToDoListView.as_view(), name='show_tasklist'),

    # add task
    path('add_task/', views.add_task, name='add_task'),
]