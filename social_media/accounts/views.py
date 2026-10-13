from django.shortcuts import render
from accounts.serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet,ModelViewSet
from accounts.models import *
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class SignUpView(ViewSet):
    def create(self,request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        delete_id = self.kwargs.get("pk")
        CustomUser.objects.get(id=delete_id).delete()
        return Response(data={"Data is deleted"})

class LoginView(ViewSet):
    def create(self,request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username,password=password)
        if user:
            token,created = Token.objects.get_or_create(user=user)
            return Response(data={"msg":"Login succesfully complated","created":created,"token":token.key,"username":user.username,"user_id":user.id},status=status.HTTP_201_CREATED)
        return Response(data={"msg":"Invalid request data"},status=status.HTTP_400_BAD_REQUEST)

class ProfileView(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    #queryset = CustomUser.objects.all()

    def list(self,request):
        serializer = UserSerializer(request.user)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def update(self,request,pk=None):
        serializer = UserSerializer(request.user,data = request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
