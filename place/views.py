from django.shortcuts import render, redirect
from .models import PlaceModel, PlaceComment
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView

# Create your views here.
def home(request):
    user = request.user.is_authenticated
    if user:
        return
    else:
        return

def place(request):
    return

@login_required
def delete_place(request):
    return

@login_required
def detail_place(request):
    return

@login_required
def write_comment(request):
    return

@login_required
def delete_comment(request):
    return