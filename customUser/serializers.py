from rest_framework.validators import UniqueValidator
from rest_framework import serializers

from django.db.models.query import QuerySet
from django.contrib.auth.models import User
from customUser.models import CustomUser
from django.contrib.auth.password_validation import validate_password

class SignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    username = serializers.CharField(
        max_length=50,
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = CustomUser
        fields = ('password', 'confirm', 'username', 'email', 'first_name','author_pseudonym')
        extra_kwargs = {'password': {'write_only': True},'confirm': {'write_only': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm']:
            raise serializers.ValidationError({"password": "Passwords didn't match!"})

        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm')
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()

        return user