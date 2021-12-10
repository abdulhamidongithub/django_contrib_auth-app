from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from .models import Client

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        l = request.POST.get("login")
        p = request.POST.get("password")
        print(p, l)
        user = authenticate(request, username=l, password=p)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
    def post(self, request):
        user1 = User.objects.create_user(
            username=request.POST.get("login"),
            password=request.POST.get("parol")
        )
        Client.objects.create(
            name = request.POST.get("name"),
            age = request.POST.get("age"),
            gender = request.POST.get("gender"),
            user = user1
        )
        login(request, user1)
        return redirect("home")
class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'home.html')
        else:
            return redirect("login")

def logoutView(request):
    logout(request)
    return redirect("login")