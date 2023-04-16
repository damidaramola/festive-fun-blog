from django.shortcuts import render
from .models import Post

# Create your views here.

# home page listing all posts 


def home_list(request):
    return render(request, 'index.html')