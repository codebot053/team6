from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_up_view(request):
    return

def sign_in_view(request):
    return

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

def tags(request):
    return