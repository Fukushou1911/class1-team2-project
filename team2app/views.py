<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment

=======
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
>>>>>>> 32ebcd5a2fd550772b2b0ed982a1c06e1cf50899

def index(request):
	return render(request, 'index.html')