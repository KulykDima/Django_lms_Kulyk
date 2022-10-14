from django.urls import path

from Courses.views import create_course
from Courses.views import delete_course
from Courses.views import detail_course
from Courses.views import edit_course
from Courses.views import get_course


app_name = 'course'

urlpatterns = [

    path('', get_course, name='list'),
    path('detail/<int:course_id>', detail_course, name='detail'),
    path('edit/<int:course_id>', edit_course, name='edit'),
    path('create/', create_course, name='create'),
    path('delete/<int:course_id>', delete_course, name='delete'),
    ]