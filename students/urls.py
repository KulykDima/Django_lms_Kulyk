
from django.urls import path


from students.views import create_student, delete_student, detail_student
from students.views import edit_student
from students.views import get_students

app_name = 'student'

urlpatterns = [
    path('', get_students, name='list'),
    path('create/', create_student, name='create'),
    path('edit/<int:student_id>', edit_student, name='edit'),
    path('details/<int:student_id>', detail_student, name='detail'),
    path('delete/<int:student_id>', delete_student, name='delete'),

]

# https://docs.djangoproject.com:8000/   en/4.1/topics/http/urls/
