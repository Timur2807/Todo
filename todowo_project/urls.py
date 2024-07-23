"""
URL configuration for todowo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from todo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('signupuser/', signupuser, name='signupuser'),
    path('welcome/', welcome, name='welcome'),
    path('logout/', logout_user, name='logout_user'),
    path('login/', login_user, name='login_user'),
    path('create/', create_todo, name='create_todo'),
    path('current/', current_todos, name='current_todo'),
    path('current/<int:pk>/', todo_details, name='todo_details'),
    path('current/<int:pk>/delete/', todo_delete, name='todo_delete'),
]
