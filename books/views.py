from django.shortcuts import render
from .models import Category, Book

# Create your views here.

def all_books(request):
    books = Book.objects.all()
    return render(request, 'books/home.html', {'books': books})
