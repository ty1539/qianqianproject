from django.db import models

# Create your models here.
from users import models as umodels
class Discount(umodels.BaseModel):
    discount_name=models.CharField(max_length=100,null=True,blank=True,verbose_name='优惠券名称')
    discount_num=models.IntegerField(verbose_name='优惠券编号')
    user=models.ForeignKey(umodels.User,verbose_name='用户')
    discount_money=models.IntegerField(verbose_name='优惠券金额')
    #来源不确定
    validity_time=models.IntegerField(verbose_name='优惠券有效期')#暂定为天
    discount_status=models.BooleanField(default=False,verbose_name='优惠券状态,默认为失效')

    def __str__(self):
        return self.discount_name

    class Meta:
        verbose_name='优惠券'
        verbose_name_plural=verbose_name


