from rest_framework import serializers
from comments.models import Comments

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comments
        fields = "__all__"
        read_only_fields = ["id","owner","added_at"]