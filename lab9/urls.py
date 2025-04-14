from django.urls import path
from . import views

urlpatterns = [
    path('lab9/task1', views.task1, name='task1'),
    path('lab9/task2', views.task2, name='task2'),
    path('lab9/task3', views.task3, name='task3'),
    path('lab9/task4', views.task4, name='task4'),
]
