from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser, Group


# Create your models here.

class BaseModel(models.Model):
    """基类"""
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        abstract = True


class User(BaseModel):
    """
    用户总表
    """
    username = models.CharField(max_length=100, verbose_name='用户的姓名', null=True, blank=True)
    head_img = models.ImageField(upload_to='head_img', verbose_name='用户头像', null=True, blank=True)
    phone = models.CharField(max_length=11, verbose_name='用户手机号')
    balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='用户余额', null=True, blank=True)
    public_openid = models.CharField(max_length=100, null=True, blank=True, verbose_name='对公众号的唯一openid')
    small_opneid = models.CharField(max_length=100, null=True, blank=True, verbose_name='小程序openid')
    unionid = models.CharField(max_length=100, null=True, blank=True, verbose_name='unionid')
    all_point = models.BigIntegerField(verbose_name='用户总积分', null=True, blank=True)

    # 需要关联优惠券,xadmin中展示优惠券列表
    # 需要查看用户交易明细
    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'
        verbose_name = '微信用户'
        verbose_name_plural = verbose_name


class SysUser(AbstractUser):
    save_num = models.IntegerField(default=0, verbose_name='管理员信息保存次数')

    class Meta:
        db_table = 'sysuser'
        verbose_name = '系统管理员'
        verbose_name_plural = verbose_name


class PointsRecord(BaseModel):
    """
    积分表
    """
    user = models.ForeignKey(User, blank=True, null=True, verbose_name='用户', related_name='pointsrecord')
    point = models.BigIntegerField(verbose_name='用户积分', null=True, blank=True)
    used = models.BigIntegerField(verbose_name='使用', null=True, blank=True)
    expire = models.IntegerField(null=True, blank=True, verbose_name='过期时间')
    from store.models import StoreManage
    store = models.ForeignKey(StoreManage, null=True, blank=True, verbose_name='商店')
    status = models.IntegerField(choices=((0, '已过期'), (1, '未过期')))
    from points_mall.models import TaskManage, PointOrder
    source = models.ForeignKey(TaskManage, blank=True, null=True, verbose_name='积分任务来源')
    point_oder = models.ForeignKey(PointOrder, blank=True, null=True, verbose_name='积分订单')

    def __str__(self):
        return str(self.point)

    class Meta:
        db_table = 'pointsrecord'
        verbose_name = '积分'
        verbose_name_plural = verbose_name


class ShopUser(User):
    class Meta:
        db_table = 'shopuser'
        verbose_name = "商家用户"
        verbose_name_plural = verbose_name
        proxy = True  # 不会在数据库中生成表

#
# class BackLog(Log):
#     """
#     后台日志记录
#     """
#     class Meta:
#         db_table='back_log'
#         verbose_name='日志管理'
#         verbose_name_plural=verbose_name
