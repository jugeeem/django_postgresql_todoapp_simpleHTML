"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth.views import LogoutView

from accounts import views



urlpatterns = [
    # frontページ
    path('index/', include('front.urls')),

    # ToDoアプリ
    path('todo/', include('todo.urls')),

    # ユーザー認証
    # path('accounts/', include('accounts.urls')),

    path('login/', views.Login.as_view()),
    path('logout/', LogoutView.as_view()),
    path('signup/', views.SignUpView.as_view()),
    path('account/', views.AccountUpdateView.as_view()),
    path('profile/', views.ProfileUpdateView.as_view()),


    # リダイレクト
    # path('', RedirectView.as_view(url='/index/')),

    # 管理画面
    path('admin/', admin.site.urls),
]
