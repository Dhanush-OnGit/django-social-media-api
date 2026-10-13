from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from posts.serializer import *
from posts.models import *
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class PostView(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def create(self, request, *args, **kwargs):
        dserializer = PostSerializer(data=request.data)
        if dserializer.is_valid():
            dserializer.save(owner = request.user)
            return Response(data=dserializer.data,status=status.HTTP_201_CREATED)
        return Response(data=dserializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        post = self.get_object()
        if request.user != post.owner:
            return Response(data={"error","Not a Correct user"},status=status.HTTP_401_UNAUTHORIZED)
        return super().update(request,*args,**kwargs)

    def destroy(self, request, *args, **kwargs):
        delete = self.get_object()
        if post.owner != request.user:
            return Response(data={"error","Invalid user"},status=status.HTTP_401_UNAUTHORIZED)
        delete.delete()
        return Response(data={"msg":"Post deleted"},status=status.HTTP_200_OK)
        
