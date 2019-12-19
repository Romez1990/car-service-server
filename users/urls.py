from django.urls import path

from .views import UserCreateView, UsersListView, ServiceCreateView, \
    ServicesListView

app_name = 'users'
urlpatterns = [
    path('user/', UserCreateView.as_view(), name='user.create'),
    path('users/', UsersListView.as_view(), name='user.view_list'),
    path('service/', ServiceCreateView.as_view(), name='service.create'),
    path('services/', ServicesListView.as_view(), name='service.view_list'),
]
