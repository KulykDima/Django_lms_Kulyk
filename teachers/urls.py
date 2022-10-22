from django.urls import path


from teachers.views import CreateTeacherView
from teachers.views import DeleteTeacherView
from teachers.views import DetailTeacherView
from teachers.views import ListTeacherView
from teachers.views import UpdateTeacherView

app_name = 'teacher'

urlpatterns = [
    path('', ListTeacherView.as_view(), name='list'),
    path('create/', CreateTeacherView.as_view(), name='create'),
    path('edit/<int:pk>', UpdateTeacherView.as_view(), name='edit'),
    path('details/<int:pk>', DetailTeacherView.as_view(), name='detail'),
    path('delete/<int:pk>', DeleteTeacherView.as_view(), name='delete'),
    ]
