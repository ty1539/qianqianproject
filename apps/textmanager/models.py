from django.db import models

# Create your models here.

from users.models import BaseModel,User
from store.models import StoreManage

class Textmng(BaseModel):
    """
    文本
    """
    user_agreement=models.TextField(null=True,blank=True,verbose_name='用户协议')
    point_rule=models.TextField(null=True,blank=True,verbose_name='积分规则说明')
    about_us=models.TextField(null=True,blank=True,verbose_name='关于我们')

    class Meta:
        db_table='Textmng'
        verbose_name='文本列表'
        verbose_name_plural=verbose_name

from store.models import StoreManage


class StoreApplay(StoreManage):
    """
    商户申请列表
    """
    class Meta:
        db_table = 'StoreApplay'
        verbose_name = "商家申请列表"
        verbose_name_plural = verbose_name
        proxy = True#不会在数据库中生成表


class Feedback(BaseModel):
    """
    反馈建议列表

    """
    headline=models.CharField(max_length=50,null=True,blank=True,verbose_name='标题')
    content=models.TextField(max_length=500,null=True,blank=True,verbose_name='内容')
    check_status=models.IntegerField(choices=((0,'已阅'),(1,'未阅')),verbose_name='审核状态')
    user=models.ForeignKey(User,verbose_name='用户')

    class Meta:
        db_table='Feedback'
        verbose_name='反馈建议列表'
        verbose_name_plural=verbose_name




