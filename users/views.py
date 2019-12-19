from rest_framework.generics import CreateAPIView, \
    RetrieveUpdateDestroyAPIView, ListAPIView

from .models import User, Service
from .serializer import UserDetailSerializer, ServiceSerializer, \
    ServiceDetailSerializer


class UserCreateView(CreateAPIView):
    serializer_class = UserDetailSerializer


class UsersListView(ListAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()


class UsersRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()


class ServiceCreateView(CreateAPIView):
    serializer_class = ServiceSerializer


class ServicesListView(ListAPIView):
    serializer_class = ServiceDetailSerializer
    queryset = Service.objects.all()


class ServicesRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceDetailSerializer
    queryset = Service.objects.all()
