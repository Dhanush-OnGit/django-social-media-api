from rest_framework import serializers
from accounts.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id","username","password","email","bio","profile_image"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)