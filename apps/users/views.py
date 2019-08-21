from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, status
from .models import User
from .serializers import LoginSerializer, UserInfoSerializer
from utils import wx_login, authentication
from qianqianproject import settings
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_payload_handler


class LoginViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    """
    create:微信用户授权登录
    """

    def get_serializer_class(self):
        if self.action == "create":
            return LoginSerializer
        if self.action == "list":
            return UserInfoSerializer

    def list(self, request, *args, **kwargs):
        print("get")
        return Response("ok")

    def create(self, request, *args, **kwargs):
        print("post")
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data.get("code")
        encryptedData = serializer.validated_data.get("encryptedData")
        iv = serializer.validated_data.get("iv")
        ret_dict = dict()
        try:
            userinfo = wx_login.wxlogin(code, encryptedData, iv, settings.APPID, settings.AppSecret)
        except:
            return Response({"error_msg": "用户信息错误"}, status=status.HTTP_400_BAD_REQUEST)
        openid = userinfo.get("openId")
        try:
            wx = User.objects.get(small_opneid=openid)
            print(wx.name)
        except:
            wx = User.objects.create(username=userinfo.get("nickName", ""), small_opneid=openid,
                                     head_img=userinfo.get("avatarUrl", ""), unionid=userinfo.get("unionid", ""))

        payload = jwt_payload_handler(wx)
        ret_dict["token"] = authentication.jwt_encode_handler(payload)
        ret_dict["id"] = wx.id
        return Response(ret_dict, status=status.HTTP_200_OK)
