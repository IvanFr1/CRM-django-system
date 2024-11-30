from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.views import View
# Create your views here.

class MyLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('auth_users:login')
    