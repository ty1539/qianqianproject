from rest_framework import serializers
from . import models


class CarWashSerializer(serializers.ModelSerializer):
    distance = serializers.CharField(help_text="距离")

    class Meta:
        model = models.StoreManage
        fields = ["id", "store_name", "low_five_price", "graded", "distance", "store_img", "status", "distance"]


class CarWashDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StoreManage
        fields = "__all__"


class SearchCarWashSerializer(serializers.ModelSerializer):
    distance = serializers.CharField(help_text="距离")
    class Meta:
        model = models.StoreManage
        fields = ['id', 'store_name', 'low_five_price', 'graded', 'store_img', "distance"]
