from rest_framework.generics import CreateAPIView, ListAPIView

from .models import User, Service
from .serializer import UserDetailSerializer, ServiceDetailSerializer


class UserCreateView(CreateAPIView):
    serializer_class = UserDetailSerializer


class UsersListView(ListAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()


class ServiceCreateView(CreateAPIView):
    serializer_class = ServiceDetailSerializer


class ServicesListView(ListAPIView):
    serializer_class = ServiceDetailSerializer
    queryset = Service.objects.all()
