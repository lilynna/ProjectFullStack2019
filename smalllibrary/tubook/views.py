from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Book,Transaction
from django.contrib.auth.models import User
# Create your views here.

@login_required
def Allbook(request):
    context = dict()
    context['Books'] = Book.objects.all()
    return render(request, 'Allbook.html',context)

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
    return redirect('/tubook')

def detailbook(request, pk):
    if request.method == 'POST':
        try:
            book = Book.objects.get(pk=pk)
            Transaction.objects.create(
                Book = book,
                #Actor = User,
                Action = "borrow",
            )
            return redirect('home')
        except Exception as e:
            print(e)
            raise e
    else:
        book = Book.objects.get(pk=pk)
        context = {'Book': book}
        return render(request, 'detailbook.html',context)