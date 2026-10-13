from rest_framework import serializers
from likes.models import Like

class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Like
        fields = "__all__"
        read_only_fields = ["id","owner"]