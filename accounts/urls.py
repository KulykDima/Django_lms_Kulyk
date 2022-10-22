from django.urls import path

from .views import AccountRegisterView, AccountLoginView, AccountLogoutView, account_view, AccountUpdateView

app_name = 'accounts'

urlpatterns = [
    path('register/', AccountRegisterView.as_view(), name='register'),
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout', AccountLogoutView.as_view(), name='logout'),
    path('profile/', account_view, name='profile_view'),
    path('update/', AccountUpdateView.as_view(), name='profile_update'),
    ]
