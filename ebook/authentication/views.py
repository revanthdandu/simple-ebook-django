from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib.auth.models import User
from .models import Profile
from books.models import Books
from django.contrib.auth.mixins import LoginRequiredMixin


class Login(View):
    def get(self, request):
        return render(request, 'ebookloginsignup/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')


class Signup(View):
    def get(self, request):
        return render(request, 'ebookloginsignup/signup.html')

    def post(self, request):
        email = request.POST['email']
        phone = request.POST['phonenumber']
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(
            email=email,
            username=username,
            password=password
        )

        Profile.objects.create(
            user=user,
            phone=phone
        )



        return redirect('login')



class Home(LoginRequiredMixin,View):
    login_url = ''
    redirect_field_name = 'redirect_to'
    def get(self, request):
        books = Books.objects.all()
        return render(request, 'ebookhome/home.html', {'books' : books})



def logout_user(request):
    logout(request)
    return redirect('login')

