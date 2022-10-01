from django.urls import path


from teachers.views import create_teacher
from teachers.views import delete_teacher
from teachers.views import detail_teacher
from teachers.views import edit_teacher
from teachers.views import get_teachers

app_name = 'teacher'

urlpatterns = [
    path('', get_teachers, name='list'),
    path('create/', create_teacher, name='create'),
    path('edit/<int:teacher_id>', edit_teacher, name='edit'),
    path('details/<int:teacher_id>', detail_teacher, name='detail'),
    path('delete/<int:teacher_id>', delete_teacher, name='delete'),
    ]
