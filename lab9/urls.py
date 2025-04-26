from django.urls import path
from . import views

urlpatterns = [
    path('lab9/task1', views.task1, name='task1'),
    path('lab9/task2', views.task2, name='task2'),
    path('lab9/task3', views.task3, name='task3'),
    path('lab9/task4', views.task4, name='task4'),

    path('lab9_part1/listbooks', views.list_books, name='list_books'),
    path('lab9_part1/addbook', views.add_book, name='add_book'),
    path('lab9_part1/editbook/<int:id>', views.edit_book, name='edit_book'),
    path('lab9_part1/deletebook/<int:id>', views.delete_book, name='delete_book'),
    

    path('lab9_part2/listbooks', views.list_books_form, name='list_books_form'),
    path('lab9_part2/addbook', views.add_book_form, name='add_book_form'),
    path('lab9_part2/editbook/<int:id>', views.edit_book_form, name='edit_book_form'),
    path('lab9_part2/deletebook/<int:id>', views.delete_book_form, name='delete_book_form'),

]
