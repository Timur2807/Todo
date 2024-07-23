from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUserCreateForm, ToDO
from .forms import *
# Create your views here.

def signupuser(request):
    if request.method == 'POST':
        form = CustomUserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('welcome')
        else:
            context = {
                'form': form,
                'error': form.errors
            }
            return render(request, 'todo/signupuser.html', context)
    else:
        form = CustomUserCreateForm()
        context = {
            'form': form
        }
        return render(request, 'todo/signupuser.html', context)


def welcome(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'todo/welcome.html', context)

def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

def home(request):
    return render(request, 'todo/home.html')

def login_user(request):
    if request.method == 'GET':
        context = {
            'form': AuthenticationForm()
        }
        return render(request, 'todo/login_user.html', context)
    else:
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            context = {
                'form': AuthenticationForm(),
                'error': 'Неверные данные'
            }
            return render(request, 'todo/login_user.html', context)
        else:
            login(request, user)
            return redirect('welcome')


def create_todo(request):
    if request.method == 'GET':
        context = {
            'form': ToDOForm()
        }
        return render(request, 'todo/create_todo.html', context)
    else:
        form = ToDOForm(request.POST)
        newtodo = form.save(commit=False)
        newtodo.user = request.user
        newtodo.save()
        return redirect('current_todo')


def current_todos(request):
    todos = ToDO.objects.filter(user=request.user)
    context = {
        'todos': todos
    }
    return render(request, 'todo/current_todo.html', context)


def todo_details(request, pk):
    todo = get_object_or_404(ToDO, pk=pk, user=request.user)
    if request.method == "GET":
        form = ToDOForm(instance=todo)
        context = {
            'todo': todo,
            'form': form
        }
        return render(request, 'todo/todo_details.html', context)


def todo_delete(request, pk):
    if request.method =="GET":
        todo = ToDO.objects.get(pk=pk, user=request.user)
        context = {
            'todo': todo
        }
        return render(request, 'todo/todo_delete.html', context)
    else:
        todo = ToDO.objects.filter(pk=pk, user=request.user).delete()
        return redirect('current_todo')

