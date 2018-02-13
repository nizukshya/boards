# Create your views here.
from django.shortcuts import render
from .models import Book
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import BookForm


def book_create(request):
    form = BookForm()
    context = {'form': form}
    html_form = render_to_string('books/includes/partial_book_create.html',
                                 context,
                                 request=request,
                                 )
    return JsonResponse({'html_form': html_form})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})
