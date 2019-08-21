from django.db import models

# Create your models here.
from users import models as umodels
from DjangoUeditor.models import UEditorField


class StoreManage(umodels.BaseModel):
    """
    门店管理
    """

    user = models.ManyToManyField(umodels.User, through='Store2User', through_fields=('store', 'user'),
                                  verbose_name='微信用户')

    linkman = models.CharField(max_length=20, blank=True, null=True, verbose_name='联系人姓名')
    store_name = models.CharField(max_length=20, verbose_name='店名', null=True, blank=True)
    store_add = models.CharField(max_length=100, verbose_name='店铺地址')
    up_five_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='5座以上价格')
    low_five_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='5座以下价格')
    service = models.CharField(max_length=4, choices=(('标准洗车', 0), ('精致洗车', 1)), verbose_name='服务内容选择')
    graded = models.CharField(verbose_name='评分', max_length=5, blank=True, null=True)
    area = models.CharField(max_length=20, blank=True, null=True, verbose_name='区域')
    location = models.CharField(max_length=100, null=True, blank=True, verbose_name='定位')
    office_hours = models.TimeField(blank=True, null=True, verbose_name='上班时间')
    closing_time = models.TimeField(blank=True, null=True, verbose_name='下班时间')
    commission_rate = models.DecimalField(max_digits=5, decimal_places=4, verbose_name='佣金比例')
    account = models.CharField(max_length=50, verbose_name='账号')  # 账户具体意思不明确
    password = models.CharField(max_length=20, null=True, blank=True, verbose_name='密码')  # 密码具体意思不明确
    bank_num = models.IntegerField(verbose_name='银行卡号', blank=True, null=True)
    cardholder = models.CharField(max_length=20, verbose_name='持卡人', blank=True, null=True)
    belong_bank = models.CharField(max_length=100, blank=True, null=True, verbose_name='所属银行')
    service_content = models.TextField(blank=True, null=True, verbose_name='服务内容')
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name='联系电话')  # 需要确认是否为商家的唯一电话
    logo = models.ImageField(upload_to='media/store/logo', verbose_name='店铺的logo', null=True, blank=True)
    store_img = models.ImageField(upload_to='media/store', null=True, blank=True, verbose_name='店铺图片')
    detail = UEditorField(verbose_name="门店详情", width=600, height=300, imagePath="book/ueditor/",
                          filePath="book/ueditor/", default='')
    audit_status = models.IntegerField(choices=((0, '通过审核',), (1, '未通过审核')), default='未通过审核', verbose_name='审核状态')
    status = models.SmallIntegerField(choices=((1, "空闲",), (2, "忙碌",), (3, "休息",)), default=1, verbose_name="商家状态")
    shop_lon = models.FloatField(blank=True, null=True, verbose_name='店铺经度')
    shop_lat = models.FloatField(blank=True, null=True, verbose_name='店铺维度')
    sub_store_manager = models.ForeignKey('self', null=True, blank=True, verbose_name='子账户')
    all_service_charge = models.PositiveIntegerField(null=True, blank=True, verbose_name='总手续费(单位分)')
    balance = models.PositiveIntegerField(null=True, blank=True, verbose_name='余额(单位分)')

    def __str__(self):
        return self.store_name

    class Meta:
        db_table = 'store'
        verbose_name = '门店'
        verbose_name_plural = verbose_name


class Store2User(umodels.BaseModel):
    """
    商家钱包流水/用户钱包流水/此为用户和商家多对多关系表
    """
    store = models.ForeignKey(StoreManage, on_delete=models.CASCADE)
    user = models.ForeignKey(umodels.User, on_delete=models.CASCADE)

    store_water_num = models.IntegerField(blank=True, null=True, verbose_name='流水编号')
    store_source = models.IntegerField(choices=((0, '洗车'), (1, '活动'), (2, '提现'), (3, '核销')), null=True, blank=True,
                                       verbose_name='来源')
    store_money = models.PositiveIntegerField(blank=True, null=True, verbose_name='交易金额(单位分)')

    user_water_num = models.IntegerField(blank=True, null=True, verbose_name='流水编号')
    user_source = models.IntegerField(choices=((0, '洗车'), (1, '活动'), (2, '充值')), null=True, blank=True,
                                      verbose_name='来源')
    user_money = models.PositiveIntegerField(blank=True, null=True, verbose_name='交易金额(单位分)')

    class Meta:
        db_table = 'StoreWallet'
        verbose_name = '商家/用户钱包流水'
        verbose_name_plural = verbose_name


class UserWater(Store2User):
    class Meta:
        db_table = 'shopuser'
        verbose_name = "用户钱包流水"
        verbose_name_plural = verbose_name
        proxy = True  # 不会在数据库中生成表
