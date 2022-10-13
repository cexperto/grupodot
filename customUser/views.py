from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .models import CustomUser
from .serializers import SignupSerializer
import hashlib
from rest_framework.permissions import IsAuthenticated

class Login(ObtainAuthToken) :
    permission_classes = (IsAuthenticated,)

    def post(self, request) :
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get_or_create(user=user)

        agent = hash_agent(user.username + request.META.get('HTTP_USER_AGENT'))

        if agent:
            return Response({
                'token': token[0].key,
                'user_id': user.pk,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'author_pseudonym':user.author_pseudonym,
                'email': user.email,
                'is_admin': user.is_superuser,
                'is_staff': user.is_staff,
                'is_active': user.is_active,
                'verified': True
            })
        else:
            return Response({
                'user_id': user.pk,
                'token': token[0].key,
                'verified': False
            })

class Signup(generics.CreateAPIView) :
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        token = Token.objects.get_or_create(user=user)

        agent = hash_agent(user.username + request.META.get('HTTP_USER_AGENT'))

        if agent:
            return Response({
                'user_id': user.pk,
                'email': user.email,
                'username': user.email,                
            })

class Validation(generics.CreateAPIView) :
    def post(self, request) :
        user = CustomUser.objects.get(pk=request.data.get('user_id'))

        agent = hash_agent(user.username + request.META.get('HTTP_USER_AGENT'))
        
        if agent:
        
            return Response({
                'user_id': user.pk,
                'username': user.name,
                'email': user.email,
                'is_admin': user.is_superuser,
                'is_staff': user.is_staff,
                'is_active': user.is_active,
                'verified': True
            })

        else :
            return Response({
                'error': "error"
            })


def hash_agent(string=''):
    return hashlib.md5(bytes(string, encoding='utf8')).hexdigest()