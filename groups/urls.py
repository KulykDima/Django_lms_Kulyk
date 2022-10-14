from django.urls import path

from groups.views import create_group
from groups.views import delete_group
from groups.views import detail_group
from groups.views import ListGroupView
from groups.views import UpdateGroupView

app_name = 'group'

urlpatterns = [

    path('', ListGroupView.as_view(), name='list'),
    path('detail/<int:group_id>', detail_group, name='detail'),
    path('edit/<int:pk>', UpdateGroupView.as_view(), name='edit'),
    path('create/', create_group, name='create'),
    path('delete/<int:group_id>', delete_group, name='delete'),
    ]
