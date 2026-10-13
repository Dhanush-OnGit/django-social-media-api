from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from followers.serializer import FollowersSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from followers.models import Followers
# Create your views here.

class FollowerView(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FollowersSerializer
    queryset = Followers.objects.all()

    def create(self, request, *args, **kwargs):
        dserilaizer = FollowersSerializer(data=request.data)
        if dserilaizer.is_valid():
            user = dserilaizer.validated_data["following"]
            if user == request.user:
                return Response(data={"not follow yourself"},status=status.HTTP_400_BAD_REQUEST)
            already_followed = Followers.objects.filter(following = request.user,follower = user).exists()
            if already_followed:
                return Response(data={"error":"You are already followed"},status=status.HTTP_403_FORBIDDEN)
            dserilaizer.save(follower=request.user)
            return Response(data={"msg":"Followed"},status=status.HTTP_201_CREATED)
        return Response(data={"error":"the data is in_valid provide request data"},status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        follower = self.get_object()
        if follower.follower != request.user and follower.following != request.user:
            return Response(data={"error":"not have a access to unfollow"})
        follower.delete()
        return Response(data={"msg":"They unfollowed"},status=status.HTTP_200_OK)
