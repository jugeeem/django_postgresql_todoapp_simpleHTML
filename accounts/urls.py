from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [
    # login
    path('/login/', views.Login.as_view(), name='login'),
    
    # logout
    path('/logout/', LogoutView.as_view(), name='logout'),
    
    # signup
    path('/signup/', views.SignUpView.as_view(), name='signup'),
    
    # account
    path('/account/', views.AccountUpdateView.as_view(), name='account'),
    
    # profile
    path('/profile/', views.ProfileUpdateView.as_view(), name='profile'),
]
