"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from groups.views import detail_group
from groups.views import edit_group
from groups.views import get_groups

from students.views import create_student, detail_student
from students.views import edit_student
from students.views import get_students
from students.views import index

from teachers.views import detail_teacher
from teachers.views import edit_teacher
from teachers.views import get_teachers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('students/', get_students),
    path('students/create/', create_student),
    path('students/edit/<int:student_id>', edit_student),
    path('students/details/<int:student_id>', detail_student),
    path('groups/', get_groups),
    path('groups/detail/<int:group_id>', detail_group),
    path('groups/edit/<int:group_id>', edit_group),
    path('teachers/', get_teachers),
    path('teachers/detail/<int:teacher_id>', detail_teacher),
    path('teachers/edit/<int:teacher_id>', edit_teacher),
]

# https://docs.djangoproject.com:8000/   en/4.1/topics/http/urls/
