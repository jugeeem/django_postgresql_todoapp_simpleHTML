from django.urls import path
from . import views


urlpatterns = [
    # show tasklist
    path('tasklist/', views.ToDoListView.as_view(), name='show_tasklist'),

    # show directorlist
    path('directorlist/', views.DirectorListView.as_view(), name='show_directorlist'),

    # show task detail
    path('taskdetail/<int:pk>/', views.TaskDetailView.as_view(), name='show_taskdetail'),

    # add task
    path('add_task/', views.TaskCreateView.as_view(), name='add_task'),

    # add director
    path('add_director/', views.DirectorCreateView.as_view(), name='add_director'),

    # update task
    path('update_task/<int:pk>/', views.UpdateTaskView.as_view(), name='update_task'),

    # update director
    path('update_director/<int:pk>/', views.UpdateDirectorView.as_view(), name='update_director'), 

    # delete task
    path('delete_task/<int:pk>/', views.DeleteTaskView.as_view(), name='delete_task'),

    # delete director
    path('delete_director/<int:pk>/', views.DeleteDirectorView.as_view(), name='delete_director'),
]