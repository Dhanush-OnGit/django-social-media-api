from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from comments.models import *
from comments.serializer import CommentSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class CommentView(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()

    def create(self, request, *args, **kwargs):
        dserializer = CommentSerializer(data = request.data)
        if dserializer.is_valid():
            dserializer.save(owner = request.user)
            return Response(data=dserializer.data,status=status.HTTP_201_CREATED)
        return Response(data=dserializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        update = self.get_object()
        if update.owner != request.user:
            return Response(data={"error":"the user is invalid"},status=status.HTTP_401_UNAUTHORIZED)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.owner != request.user and comment.post_obj.owner != request.user:
            return Response(data={"error":"The user is wrong"},status=status.HTTP_401_UNAUTHORIZED)
        comment.delete()
        return Response(data={"msg":"teh comment is deleted"},status=status.HTTP_200_OK)
