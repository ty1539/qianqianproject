from django.shortcuts import render
from rest_framework import mixins, status
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from . import serializers
from .models import StoreManage
from utils import tools


# Create your views here.

class RecentCarWashViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    list:按距离由近到远的商家
    """

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.CarWashSerializer
        if self.action == "retrieve":
            return serializers.CarWashDetailSerializer

    def list(self, request, *args, **kwargs):
        lon = request.query_params.get("lon")
        lat = request.query_params.get("lat")
        start = request.query_params.get("start", 0)
        limit = request.query_params.get("limit", 2)
        key = request.query_params.get("key", "graded desc, distance, low_five_price")
        status_id = request.query_params.get("status", " <= 3")
        try:
            start = int(start)
            limit = int(limit)
        except:
            return Response({"msg": "参数类型错误"}, status=status.HTTP_400_BAD_REQUEST)
        if status_id != " <= 3" and status_id.isdigit():
            status_id = "= " + str(status_id)
        elif status_id != " <= 3" and not status_id.isdigit():
            return Response({"msg": "参数错误"}, status=status.HTTP_400_BAD_REQUEST)
        if key == "graded":
            key += " desc"
        sql = "select" \
              " id," \
              " store_name," \
              " low_five_price," \
              " graded," \
              " store_img," \
              " status," \
              " audit_status,(" \
              "6371 * acos(" \
              "cos(" \
              "radians({lat})) * cos(" \
              "radians(store_lat)) * cos(" \
              "radians(store_lon) - radians({lon})) + sin(" \
              "radians({lat})) * sin(" \
              "radians(store_lat))) " \
              " ) AS distance " \
              "FROM" \
              " store " \
              "HAVING " \
              "distance < 3 " \
              "and audit_status = 0 " \
              "and status {status} " \
              "ORDER BY " \
              "{key} " \
              "LIMIT {start}, " \
              "{limit}".format(lat=lat, lon=lon, status=status_id, key=key, start=start, limit=limit)

        shop_list = StoreManage.objects.raw(sql)
        serializer = self.get_serializer(shop_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SearchCarWashViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    list:返回模糊查询的商家列表
    """

    serializer_class = serializers.SearchCarWashSerializer

    def list(self, request, *args, **kwargs):
        keyword = request.query_params.get("keyword").strip()
        shop_list = StoreManage.objects.filter(store_name__icontains=keyword)
        shop_count = shop_list.__len__()
        if not shop_count:
            return Response({"msg": "未查询到相关商家信息"}, status=status.HTTP_200_OK)
        if shop_count == 1:
            serializer = self.get_serializer(shop_list.first())
        else:
            serializer = self.get_serializer(shop_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RecentCarWashViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    """
    list:按距离由近到远的商家
    """

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.CarWashSerializer
        if self.action == "retrieve":
            return serializers.CarWashDetailSerializer

    def list(self, request, *args, **kwargs):
        lon = request.query_params.get("lon")
        lat = request.query_params.get("lat")
        start = request.query_params.get("start", 0)
        limit = request.query_params.get("limit", 2)
        key = request.query_params.get("key", "graded desc, distance, low_five_price")
        status_id = request.query_params.get("status", " <= 3")
        try:
            start = int(start)
            limit = int(limit)
        except:
            return Response({"msg": "参数类型错误"}, status=status.HTTP_400_BAD_REQUEST)
        if status_id != " <= 3" and status_id.isdigit():
            status_id = "= " + str(status_id)
        elif status_id != " <= 3" and not status_id.isdigit():
            return Response({"msg": "参数错误"}, status=status.HTTP_400_BAD_REQUEST)
        if key == "graded":
            key += " desc"
        sql = "select" \
              " id," \
              " store_name," \
              " low_five_price," \
              " graded," \
              " store_img," \
              " status," \
              " audit_status,(" \
              "6371 * acos(" \
              "cos(" \
              "radians({lat})) * cos(" \
              "radians(store_lat)) * cos(" \
              "radians(store_lon) - radians({lon})) + sin(" \
              "radians({lat})) * sin(" \
              "radians(store_lat))) " \
              " ) AS distance " \
              "FROM" \
              " store " \
              "HAVING " \
              "distance < 3 " \
              "and audit_status = 0 " \
              "and status {status} " \
              "ORDER BY " \
              "{key} " \
              "LIMIT {start}, " \
              "{limit}".format(lat=lat, lon=lon, status=status_id, key=key, start=start, limit=limit)

        shop_list = StoreManage.objects.raw(sql)
        serializer = self.get_serializer(shop_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
