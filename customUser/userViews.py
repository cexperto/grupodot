from customUser.models import CustomUser
from rest_framework import generics, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .userSerializer import UserSerializer
from rest_framework.views import APIView
from django.http import HttpResponse, Http404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class UserList(generics.ListAPIView):
    
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class CustomUserList(APIView):
    permission_classes = (IsAuthenticated,)
    def get_object(self,pk):
        try:
            return CustomUser.objects.get(pk = pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        users = self.get_object(pk)
        serializer = UserSerializer(users)
        return Response(serializer.data)


    def put(self, request, pk, format=None):        
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('update success')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        if user:
            user.able = 0
            user.save()
            return Response(
                {
                    "message": "delete success"
                },
                status=status.HTTP_200_OK
            )
        return Response({"error": "The Activity not found"}, status=status.HTTP_404_NOT_FOUND)

class AllUsers(APIView):

    def get(self, request):
        users = CustomUser.objects.all().order_by('id')
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)