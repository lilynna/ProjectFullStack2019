from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Book
# Create your views here.

@login_required
def Allbook(request):
    context = dict()
    context['Books'] = Book.objects.all()
    return render(request, 'Allbook.html')

def home(request):
    context = dict()

    if request.user.is_authenticated:
        context['greeting'] = 'Welcome Back {}'.format(request.user)
    else:
        context['greeting'] = 'Welcome Anonymous'

    return render(request, 'home.html', context)

@login_required
def logoutView(request):
    logout(request)
    return redirect('/example')

def list_book(request):
    context = dict()
    context['book'] = Book.objects.all().order_by('book')
    return render(request,'listbook.html',context)

