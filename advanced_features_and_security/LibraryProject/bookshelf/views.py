from django.shortcuts import render

# Create your views here.
["book_list", "raise_exception", "books"]

# views.py
from django.db import connection

def search_books(request):
    query = request.GET.get('q', '')
    sql_query = f"SELECT * FROM bookshelf_book WHERE title LIKE '%{query}%'"
    with connection.cursor() as cursor:
        cursor.execute(sql_query)
        results = cursor.fetchall()

# views.py
from django.shortcuts import render
from .models import Book

def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query)  # Properly parameterized
    return render(request, 'bookshelf/book_list.html', {'books': books})

["from .forms import ExampleForm"]
from django.shortcuts import render
from .models import Book
from .forms import BookSearchForm

def search_books(request):
    form = BookSearchForm(request.GET)
    books = None
    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(title__icontains=query)

    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})
