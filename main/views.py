from django.shortcuts import render, HttpResponse
from .models import ToDo
from .models import Book
# Create your views here.

def homepage(request):
    return render (request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def second(request):
    return HttpResponse("test 2 page")

def books(request):
    book_list = Book.objects.all()
    return render(request, "books.html", {"books_list": book_list})

def homework31a(request):
    return render (request, "homework31.html")

def homework31b(request):
    return render (request, "hw31b.html")

def homework31c(request):
    return render (request, "hw31c.html")