from django.urls import path

from groups.views import create_group
from groups.views import delete_group
from groups.views import detail_group
from groups.views import edit_group
from groups.views import get_groups


app_name = 'group'

urlpatterns = [

    path('', get_groups, name='list'),
    path('detail/<int:group_id>', detail_group, name='detail'),
    path('edit/<int:group_id>', edit_group, name='edit'),
    path('create/', create_group, name='create'),
    path('delete/<int:group_id>', delete_group, name='delete'),
    ]
