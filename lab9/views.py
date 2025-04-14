from django.shortcuts import render
from .models import Department, Course, Student
from django.db.models import Count
from django.db.models import Min


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
