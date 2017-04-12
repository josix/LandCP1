from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return render_to_response("registration/my_login.html")

def sign_up_page(request):
    return render_to_response("registration/sign_up.html")

def my_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect("/roll_call/")
        else:
            message = "用戶名、密碼錯誤"
            return render_to_response("registration/my_login.html", locals())
    else:
        return render_to_response("registration/my_login.html", locals())

def sign_up(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username, email, password)
        #user.is_staff = True
        user.save()
        message = "註冊成功"
        return render_to_response("registration/my_login.html", locals())

    return render_to_response("registration/sign_up.html")

