from django.db import models

# Create your models here.

class BaseModel(models.Model):
    """基类"""
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        abstract = True

class System(BaseModel):

    """
    系统设置
    """
    title = models.CharField(max_length=255,null=True,blank=True,verbose_name='网站标题')
    keywords = models.CharField(max_length=255,null=True,blank=True,verbose_name='网站关键字')
    description = models.TextField(max_length=500,null=True,blank=True,verbose_name='网站描述')
    logo = models.ImageField(upload_to='system',null=True,blank=True,verbose_name='网站logo')
    address = models.CharField(max_length=255,null=True,blank=True,verbose_name='地址')
    jifen_chongzhi = models.IntegerField(blank=True, null=True,verbose_name='积分重置日期')
    jifen_max = models.FloatField(blank=True, null=True,verbose_name='每日积分上限')
    qrcode_day = models.IntegerField(blank=True, null=True,verbose_name='二维码有效期')
    email = models.CharField(max_length=100, blank=True, null=True,verbose_name='邮箱')
    beiancode = models.CharField(max_length=100, blank=True, null=True,verbose_name='备案号')
    wechat = models.CharField(max_length=100, blank=True, null=True,verbose_name='微信')
    company_name = models.CharField(max_length=100, blank=True, null=True,verbose_name='公司名称')
    phone=models.IntegerField(blank=True,null=True,verbose_name='联系电话')


    def __str__(self):
        return self.title
    class Meta:
        db_table='system'
        verbose_name='网站设置'
        verbose_name_plural=verbose_name


class Recharge(BaseModel):
    """
    充值金额
    """
    system=models.ForeignKey(System,null=True,blank=True,verbose_name='系统')
    money=models.PositiveIntegerField(null=True,verbose_name='充值金额')

    def __str__(self):
        return self.money

    class Meta:
        db_table='Recharge'
        verbose_name='充值金额'
        verbose_name_plural=verbose_name



class Qrcode(System):
    class Meta:
        verbose_name = "二维码设置"
        verbose_name_plural = verbose_name
        proxy = True#不会在数据库中生成表



class SetPoint(System):
    class Meta:
        verbose_name = "积分设置"
        verbose_name_plural = verbose_name
        proxy = True#不会在数据库中生成表