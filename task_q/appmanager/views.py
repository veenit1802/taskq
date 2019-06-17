from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .form import TaskForm


def login_form(request):
    """
    description: this function render's the login page
    author: veenit kumar sukla
    :param request: request
    :return:render
    :Method allowed: GET
    """
    return render(request, 'login.html')


def login_check(request):
    """
    description: this function authenticate the user
    author: veenit kumar shukla
    :param request: request
    :return: Redirect
    :Method allowed: POST
    """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            print("user exists")
            return HttpResponseRedirect('/home')
        else:
            print("user does not exists")
            return HttpResponseRedirect('/login')


def sign_up(request):
    """
    description: this function render's the signup page
    author: veenit kumar shukla
    :param request: request
    :return: render
    :Method allowed: GET
    """
    return render(request, 'signup.html')


def create_user(request):
    """
    description:takes the input from the signup page and create the user account
    author: veenit kumar shukla
    :param request: request
    :return: redirect
    :Method allowed: POST
    """
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            User.objects.create_user(username, email, password)
            print("user created")
            return HttpResponseRedirect('login')
        except Exception as e:
            print("user already exists")
            return HttpResponseRedirect('signup')


def reset_user(request):
    """
    description: this function render's the reset page
    author: veenit kumar shukla
    :param request: request
    :return: render
    :Method allowed: GET
    """
    return render(request, 're.html')


def reset_password(request):
    """
    description:changes the user account password as per user need                                                                                  
    author: veenit kumar shukla
    :param request: request
    :return: redirect
    :Method allowed: POST
    """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            print("password changed")
        except Exception as e:
            print("username is wrong")
    return HttpResponseRedirect('/login')


def home(request):
    """
    description: this function render's the home page
    author: veenit kumar shukla
    :param request:  request
    :return: render
    :Method allowed: GET
    """
    data = TaskForm()
    return render(request, 'home.html', {"task_create_form": data})


def home_save_data(request):
    """
    description: this function saves the data in database
    author: veenit kumar shukla
    :param request: request
    :return: redirect
    :Method allowed: POST
    """
    if request.method == "POST":
        obj = TaskForm(request.POST)
        obj.save()
    return HttpResponseRedirect('/home')
