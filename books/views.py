from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Category, Book

# Create your views here.


@login_required(login_url='/auth/login')
def home(request):
    books = Book.objects.all()
    return render(request, 'library/home.html', {'books': books})


def book_all(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'library/books/index.html', {'books': books})


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    is_favourite = book.favourite.filter(id=request.user.id).exists()
    context = {
        'book': book,
        'is_favourite': is_favourite,
    }
    return render(request, 'library/books/detail.html', context)


def book_filter_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    books = Book.objects.filter(category=category).order_by('title')
    return render(request, 'library/books/category.html', {'category': category, 'books': books})


def book_searching(req):
    keyword = req.GET.get('keyword')
    books = Book.objects.filter(title__icontains=keyword)
    context = {
        'keyword': keyword,
        'books': books.order_by('title'),
    }
    
    return render(req, 'library/books/index.html', context)


def favourite_all(request):
    books = request.user.favourite_books.all()
    return render(request, 'library/favourite/favourite.html', {'books': books})


def favourite_add(request):
    if request.POST.get('action') == 'post':
        book_id = int(request.POST.get('book_id'))
        book = get_object_or_404(Book, id=book_id)
        book.favourite.add(request.user)
        favourite_quantity = request.user.favourite_books.all().count()
        is_favourite = book.favourite.filter(id=request.user.id).exists()
        context = {
            'favourite_quantity': favourite_quantity,
            'is_favourite': is_favourite,
        }
        response = JsonResponse(context)
        return response


def favourite_delete(request):
    if request.POST.get('action') == 'post':
        book_id = int(request.POST.get('book_id'))
        book = get_object_or_404(Book, id=book_id)
        book.favourite.remove(request.user)
        favourite_quantity = request.user.favourite_books.all().count()
        is_favourite = book.favourite.filter(id=request.user.id).exists()
        context = {
            'favourite_quantity': favourite_quantity,
            'is_favourite': is_favourite,
        }
        response = JsonResponse(context)
        return response
