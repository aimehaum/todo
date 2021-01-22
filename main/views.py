from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo
from .models import Book


def homepage(request):
    return render (request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def second(request):
    return HttpResponse("test 2 page")

def books(request):
    book_list = Book.objects.all()
    return render(request, "books.html", {"book_list": book_list})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = not todo.is_favorite
    todo.save()
    return redirect(test)

def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)


def add_book(request):
    form = request.POST
    title = form["book_title"]
    subtitle = form["book_subtitle"]
    description = form["book_description"]
    price = form["book_price"]
    genre = form["book_genre"]
    author = form["book_author"]
    year = form["book_year"]
    book = Book(title=title, subtitle=subtitle, description=description, price=price, genre=genre, author=author, year=year)
    book.save()
    return redirect(books)

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect(books)

def mark_book(request, id):
    book = Book.objects.get(id=id)
    book.isfavorite = not book.isfavorite
    book.save()
    return redirect(books)


def BooksDetail(request, id):
    book = Book.objects.get(id=id)
    return render (request, "books_detail.html", {"book": book})


def homework31a(request):
    return render (request, "homework31.html")

def homework31b(request):
    return render (request, "hw31b.html")

def homework31c(request):
    return render (request, "hw31c.html")


