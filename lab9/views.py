from django.shortcuts import render
from .models import Department, Course, Student
from django.db.models import Count
from django.db.models import Min
from .forms import BookForm
from django.shortcuts import get_object_or_404
from .models import Book
from django.shortcuts import render, redirect, get_object_or_404




def task1(request):
    departments = Department.objects.annotate(num_students=Count('student'))
    return render(request, 'lab9/task1.html', {'departments': departments})

def task2(request):
    courses = Course.objects.annotate(num_students=Count('student'))
    return render(request, 'lab9/task2.html', {'courses': courses})

def task3(request):
    departments = Department.objects.annotate(
        oldest_student_id=Min('student__id')
    )
    return render(request, 'lab9/task3.html', {'departments': departments})

def task4(request):
    departments = Department.objects.annotate(num_students=Count('student')) \
                                    .filter(num_students__gt=2) \
                                    .order_by('-num_students')#descending 
    return render(request, 'lab9/task4.html', {'departments': departments})


def list_books(request):
    from .models import Book
    books = Book.objects.all()
    return render(request, 'lab9/listbooks.html', {'books': books})


def add_book(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']
        edition = request.POST['edition']
        Book.objects.create(title=title, author=author, price=price, edition=edition)
        return redirect('list_books')
    return render(request, 'lab9/addbook.html')


def edit_book(request, id):
    book = Book.objects.get(pk=id)
    if request.method == "POST":
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.price = request.POST['price']
        book.edition = request.POST['edition']
        book.save()
        return redirect('list_books')
    return render(request, 'lab9/editbook.html', {'book': book})


def delete_book(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect('list_books')


def list_books_form(request):
    books = Book.objects.all()
    return render(request, 'lab9/form_listbooks.html', {'books': books})


def add_book_form(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books_form')
    else:
        form = BookForm()
    return render(request, 'lab9/form_addbook.html', {'form': form})


def edit_book_form(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books_form')
    else:
        form = BookForm(instance=book)
    return render(request, 'lab9/form_editbook.html', {'form': form})


def delete_book_form(request, id):
    book = get_object_or_404(Book, pk=id)
    book.delete()
    return redirect('list_books_form')