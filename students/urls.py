
from django.urls import path


from students.views import CreateStudentView
from students.views import DeleteStudentView
from students.views import DetailStudentView
from students.views import ListStudentsView
from students.views import UpdateStudentView

app_name = 'student'

urlpatterns = [
    path('', ListStudentsView.as_view(), name='list'),
    path('create/', CreateStudentView.as_view(), name='create'),
    path('edit/<int:pk>', UpdateStudentView.as_view(), name='edit'),
    path('details/<int:pk>', DetailStudentView.as_view(), name='detail'),
    path('delete/<int:pk>', DeleteStudentView.as_view(), name='delete'),

]

# https://docs.djangoproject.com:8000/   en/4.1/topics/http/urls/
