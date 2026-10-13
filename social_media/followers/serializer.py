from rest_framework import serializers
from followers.models import Followers

class FollowersSerializer(serializers.ModelSerializer):
    follower = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Followers
        fields = "__all__"
        read_only_fields = ["id","follower","created_at"]