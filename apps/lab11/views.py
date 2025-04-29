from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm, Student2Form, GalleryForm
from .models import Student2 ,Gallery

def list_students(request):
    students = Student.objects.all()
    return render(request, 'lab11/list_students.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm()
    return render(request, 'lab11/add_student.html', {'form': form})

def edit_student(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'lab11/edit_student.html', {'form': form})

def delete_student(request, id):
    student = get_object_or_404(Student, pk=id)
    student.delete()
    return redirect('list_students')



def list_students2(request):
    students = Student2.objects.all()
    return render(request, 'lab11/list_students2.html', {'students': students})

def add_student2(request):
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students2')
    else:
        form = Student2Form()
    return render(request, 'lab11/add_student2.html', {'form': form})

def edit_student2(request, id):
    student = get_object_or_404(Student2, pk=id)
    if request.method == 'POST':
        form = Student2Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students2')
    else:
        form = Student2Form(instance=student)
    return render(request, 'lab11/edit_student2.html', {'form': form})

def delete_student2(request, id):
    student = get_object_or_404(Student2, pk=id)
    student.delete()
    return redirect('list_students2')

def gallery_list(request):
    images = Gallery.objects.all()
    return render(request, 'lab11/gallery_list.html', {'images': images})

def add_image(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery_list')
    else:
        form = GalleryForm()
    return render(request, 'lab11/add_image.html', {'form': form})
