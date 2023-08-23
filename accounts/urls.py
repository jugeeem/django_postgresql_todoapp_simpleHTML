from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [
    # signup
    path('signup/', views.SignUpCreateView.as_view(), name='signup'),

    # login
    path('login/', views.Login.as_view(), name='login'),

    # logout
    path('logout/', LogoutView.as_view(), name='logout'),

    # account
    path('account/', views.AccountUpdateView.as_view(), name='account'),

    # profile
    path('profile/', views.ProfileUpdateView.as_view(), name='profile'),
]
