from django.urls import path

from groups.views import CreateGroupView
from groups.views import DeleteGroupView
from groups.views import DetailGroupView
from groups.views import ListGroupView
from groups.views import UpdateGroupView

app_name = 'group'

urlpatterns = [

    path('', ListGroupView.as_view(), name='list'),
    path('detail/<int:pk>', DetailGroupView.as_view(), name='detail'),
    path('edit/<int:pk>', UpdateGroupView.as_view(), name='edit'),
    path('create/', CreateGroupView.as_view(), name='create'),
    path('delete/<int:pk>', DeleteGroupView.as_view(), name='delete'),
    ]
