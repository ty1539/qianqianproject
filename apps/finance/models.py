from django.db import models

# Create your models here.
from users.models import BaseModel,User
from store.models import StoreManage,Store2User

class OverApply(BaseModel):
    """
    申请提现
    """
    store=models.ForeignKey(StoreManage,null=True,blank=True,verbose_name='商店')
    check_status=models.IntegerField(choices=((0,'通过'),(1,'不通过')),verbose_name='审核状态')
    withdraw_money=models.PositiveIntegerField(null=True, blank=True, verbose_name='提现金额(单位分)')
    num=models.IntegerField(default=0,verbose_name='提现次数')
    service_money=models.PositiveIntegerField(null=True,blank=True,verbose_name='单次提现手续费(单位分)')

    class Meta:
        db_table='OverApply'
        verbose_name='申请提现列表'
        verbose_name_plural=verbose_name

class IsOverApply(OverApply):
    class Meta:
        db_table = 'IsOverApply'
        verbose_name = "已提现"
        verbose_name_plural = verbose_name
        proxy = True#不会在数据库中生成表



class UserWallet(User):
    class Meta:
        db_table = 'UserWallet'
        verbose_name = "用户钱包"
        verbose_name_plural = verbose_name
        proxy = True#不会在数据库中生成表


class StoreWallet(StoreManage):
    class Meta:
        db_table = 'StoreWallet'
        verbose_name = "商家钱包"
        verbose_name_plural = verbose_name
        proxy = True#不会在数据库中生成表

