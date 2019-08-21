from django.db import models

# Create your models here.

from users.models import User
from users import models as umodels
from store import models as smodels


class Order(umodels.BaseModel):
    """支付订单"""
    user = models.ForeignKey(User, verbose_name="微信用户", null=True, blank=True, related_name='user')
    storemanage = models.ForeignKey(smodels.StoreManage, verbose_name='门店', null=True, blank=True)
    order_sn = models.CharField(max_length=30, null=True, blank=True, unique=True, verbose_name="订单号")
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name="交易号")
    total_money = models.PositiveIntegerField(verbose_name='总金额(单位分)')
    handel_money = models.PositiveIntegerField(verbose_name='手续费(单位分)')
    user_real_money = models.PositiveIntegerField(verbose_name='用户实际支付(单位分)')
    store_real_money = models.PositiveIntegerField(verbose_name='商家实收金额(单位分)')
    pay_type = models.IntegerField(choices=((0, '微信支付'), (1, '余额支付')), verbose_name='支付方式')
    pay_status = models.IntegerField(choices=((0, '未支付'), (1, '已完成'), (2, '已取消')), verbose_name='支付状态')
    order_status = models.IntegerField(choices=((0, '已取消'), (1, '待使用'), (2, '待评价'), (3, '已完成')), verbose_name='订单状态')
    order_type = models.IntegerField(choices=((0, '洗车订单'), (1, '活动订单'), (2, '充值订单')), verbose_name='订单类型')

    def __str__(self):
        return self.order_sn

    class Meta:
        db_table = 'order'
        verbose_name = '订单'
        verbose_name_plural = verbose_name
