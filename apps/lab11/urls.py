from . import views
from django.urls import path

urlpatterns = [

path('liststudents', views.list_students, name='list_students'),
path('addstudent', views.add_student, name='add_student'),
path('editstudent/<int:id>', views.edit_student, name='edit_student'),
path('deletestudent/<int:id>', views.delete_student, name='delete_student'),

path('liststudents2', views.list_students2, name='list_students2'),
path('addstudent2', views.add_student2, name='add_student2'),
path('editstudent2/<int:id>', views.edit_student2, name='edit_student2'),
path('deletestudent2/<int:id>', views.delete_student2, name='delete_student2'),

path('gallery', views.gallery_list, name='gallery_list'),
path('gallery/add', views.add_image, name='add_image'),

]