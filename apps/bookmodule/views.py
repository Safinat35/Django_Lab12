from django.shortcuts import render
from django.http import HttpResponse
from apps.bookmodule.models import Book
from .models import Book
from django.db import models

from django.db.models import Q, Count, Sum, Avg, Max, Min
from django.shortcuts import render
from .models import Book, Student, Address


def index(request):
   return render(request, "bookmodule/index.html")

def list_books(request):
   return render(request, 'bookmodule/list_books.html')

def aboutus(request):
   return render(request, 'bookmodule/aboutus.html')

def viewbook(request, bookId):
   return render(request, 'bookmodule/one_book.html')

from .models import Book

def search_books(request):
   if request.method == "POST":
      keyword = request.POST.get('keyword', '').strip().lower()
      is_title = request.POST.get('option1')
      is_author = request.POST.get('option2')

      books = Book.objects.all()

      if keyword:
            if is_title and is_author:
               books = books.filter(
                  models.Q(title__icontains=keyword) | models.Q(author__icontains=keyword)
               )
            elif is_title:
               books = books.filter(title__icontains=keyword)
            elif is_author:
               books = books.filter(author__icontains=keyword)
            else:
               books = []

      return render(request, 'bookmodule/bookList.html', {'books': books})


   return render(request, 'bookmodule/search.html')
def __getBooksList():
   book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
   book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
   book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
   return [book1, book2, book3]

def links(request):
   return render(request, 'bookmodule/html5/links.html')
def text_formatting(request):
   return render(request, 'bookmodule/html5/text_formatting.html')
def listing(request):
   return render(request, 'bookmodule/html5/listing.html')

def tables(request):
   return render(request, 'bookmodule/html5/tables.html')


def simple_query(request):
   mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
   return render(request, 'bookmodule/bookList.html', {'books':mybooks})


def complex_query(request):
   mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
   if len(mybooks)>=1:
      return render(request, 'bookmodule/bookList.html', {'books':mybooks})
   else:
      return render(request, 'bookmodule/index.html')



def task1_view(request):
   books = Book.objects.filter(Q(price__lte=80))
   return render(request, 'bookmodule/task1.html', {'books': books})

def task2_view(request):
   books = Book.objects.filter(
      Q(edition__gt=3) & (Q(title__icontains='co') | Q(author__icontains='co'))
   )
   return render(request, 'bookmodule/task2.html', {'books': books})

def task3_view(request):
   books = Book.objects.filter(
      ~Q(edition__gt=3) & ~(Q(title__icontains='co') | Q(author__icontains='co'))
   )
   return render(request, 'bookmodule/task3.html', {'books': books})

def task4_view(request):
   books = Book.objects.all().order_by('title')
   return render(request, 'bookmodule/task4.html', {'books': books})

def task5_view(request):
   stats = Book.objects.aggregate(
      total_books=Count('id'),
      total_price=Sum('price'),
      avg_price=Avg('price'),
      max_price=Max('price'),
      min_price=Min('price')
   )
   return render(request, 'bookmodule/task5.html', {'stats': stats})

def task7_view(request):
   city_stats = Address.objects.annotate(student_count=Count('student'))
   return render(request, 'bookmodule/task7.html', {'city_stats': city_stats})