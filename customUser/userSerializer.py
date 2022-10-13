from rest_framework import serializers
from django.contrib.auth.models import User
from customUser.models import CustomUser

class UserSerializer(serializers.ModelSerializer):    

    class Meta:
        model = CustomUser
        fields = '__all__'