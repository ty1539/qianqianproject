from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.


from users import models as umodels
from discount_coupon.models import Discount

class Shopping(umodels.BaseModel):
    """
    商品管理
    """
    shopping_type = models.IntegerField(choices=((0, '实物商品'), (1, '优惠券商品')), verbose_name='商品分类')
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='商品名称')
    need_point = models.BigIntegerField(null=True, blank=True, verbose_name='商品兑换所需积分')
    color = models.CharField(max_length=100, blank=True, null=True, verbose_name='颜色')
    size = models.CharField(max_length=200, blank=True, null=True, verbose_name='规格')
    weight = models.IntegerField(default=0, verbose_name='重量')
    repertory = models.IntegerField(default=0, verbose_name='库存')
    detail = UEditorField(verbose_name=u"商品详情", width=600, height=300, imagePath="shopping/ueditor/",
                          filePath="shopping/ueditor/", default='')  # 需要使用ueditor
    # 需要外键优惠券
    discount=models.ForeignKey(Discount,null=True,blank=True,verbose_name='优惠券')
    shopping_img = models.ImageField(upload_to='media/shopping', null=True, blank=True, verbose_name='商品封面图片')
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'shopping'
        verbose_name = '商品'
        verbose_name_plural = verbose_name


class LuckyShopping(umodels.BaseModel):
    """
    抽奖商品
    """
    luckyshopping_type = models.IntegerField(choices=((0, '抽奖商品'),), verbose_name='抽奖商品类型')
    shopping = models.ForeignKey('Shopping', null=True, blank=True, verbose_name='商品')


    def __str__(self):
        return self.get_luckyshopping_type_display()
    class Meta:
        db_table = 'lucky_shopping'
        verbose_name = '抽奖商品'
        verbose_name_plural = verbose_name


class TaskManage(umodels.BaseModel):
    """
    任务
    """
    one_time_point = models.PositiveIntegerField(default=0, verbose_name='单次签到积分')
    all_month_point = models.PositiveIntegerField(default=0, verbose_name='满月获取的积分')
    invite_point = models.PositiveIntegerField(default=0, verbose_name='邀请获得积分')
    consume_point = models.PositiveIntegerField(default=0, verbose_name='消费获得积分')  # 次数不明确
    recharge_point = models.PositiveIntegerField(default=0, verbose_name='充值获得积分')
    share_point = models.PositiveIntegerField(default=0, verbose_name='分享获得积分')
    comment_point = models.PositiveIntegerField(default=0, verbose_name='评论获得积分')

    class Meta:
        db_table = 'task_manage'
        verbose_name = '任务'
        verbose_name_plural = verbose_name


class PointOrder(umodels.BaseModel):
    """
    积分商城订单
    """
    shopping = models.ForeignKey(Shopping, blank=True, null=True, verbose_name='非抽奖商品')
    luckyshopping = models.ForeignKey(LuckyShopping, blank=True, null=True, verbose_name='抽奖商品')
    user = models.ForeignKey(umodels.User, verbose_name='用户')
    phone = models.CharField(max_length=11, verbose_name='联系电话')
    # 兑换积分不明确
    order_status = models.IntegerField(choices=((0, '未发货'), (1, '已发货'), (2, '已完成')), default=0, verbose_name='积分商城订单状态')
    logistics_company = models.ForeignKey('LogisticsCompany', blank=True, null=True, verbose_name='物流公司')
    tracking_number = models.PositiveIntegerField(blank=True, null=True, verbose_name='物流单号')

    class Meta:
        db_table = 'point_order'
        verbose_name = '积分商城订单'
        verbose_name_plural = verbose_name


class LogisticsCompany(umodels.BaseModel):
    """
    物流公司
    """
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name='物流公司名称')

    class Meta:
        db_table = 'logistics_company'
        verbose_name = '物流公司'
        verbose_name_plural = verbose_name
