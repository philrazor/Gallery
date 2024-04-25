from django.shortcuts import render
from core.models import Book

def book(request):
    book_items = Book.objects.all()
    return render(request , 'core/book.html' , {
        'books_items' : book_items
    } )


# views.py
from django.shortcuts import render, redirect
from .forms import BookForm

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book')  # Redirect to the book page after successful submission
    else:
        form = BookForm()
    return render(request, 'core/add_book.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Book

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'core/book_detail.html', {'book': book})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', pk=pk)  # Redirect to book detail page after edit
    else:
        form = BookForm(instance=book)
    return render(request, 'core/edit_book.html', {'form': form, 'book': book})


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to the book list page after deletion
    return render(request, 'core/delete_book.html', {'book': book})