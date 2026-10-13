from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from likes.serializer import LikeSerializer
from likes.models import Like
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class LikeView(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def create(self, request, *args, **kwargs):
        dserialize = LikeSerializer(data=request.data)
        if dserialize.is_valid():
            post = dserialize.validated_data["post_obj"]
            already_liked = Like.objects.filter(owner=request.user,post_obj=post).exists()
            if already_liked:
                return Response(data={"error":"You already liked this post"})
            dserialize.save(owner = request.user)
            return Response(data=dserialize.data,status=status.HTTP_201_CREATED)
        return Response(data=dserialize.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        like = self.get_object()
        if like.owner != request.user:
            return Response(data={"error":"The user is not correct"},status=status.HTTP_401_UNAUTHORIZED)
        like.delete()
        return Response(data={"Like is removed"},status=status.HTTP_200_OK)
        