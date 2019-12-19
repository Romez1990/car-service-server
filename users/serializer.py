from rest_framework.serializers import ModelSerializer

from .models import User, Service


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ServiceDetailSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Service
        fields = '__all__'
