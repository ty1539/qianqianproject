from rest_framework import serializers
from .models import User


class LoginSerializer(serializers.Serializer):
    code = serializers.CharField(help_text="微信code")
    encryptedData = serializers.CharField(help_text="加密用户信息")
    iv = serializers.CharField(help_text="加密向量")


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'head_img']
