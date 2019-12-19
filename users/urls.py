from django.urls import path

from .views import UserCreateView, UsersRetrieveUpdateDestroyView, \
    UsersListView, ServiceCreateView, ServicesRetrieveUpdateDestroyView, \
    ServicesListView

app_name = 'users'
urlpatterns = [
    path('user/', UserCreateView.as_view(), name='user.create'),
    path('user/<int:pk>/', UsersRetrieveUpdateDestroyView.as_view(),
         name='user.view'),
    path('users/', UsersListView.as_view(), name='user.view_list'),
    path('service/', ServiceCreateView.as_view(), name='service.create'),
    path('service/<int:pk>/', ServicesRetrieveUpdateDestroyView.as_view(),
         name='service.view'),
    path('services/', ServicesListView.as_view(), name='service.view_list'),
]
