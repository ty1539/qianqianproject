from django.db import models

# Create your models here.
from users import models as umodels
from store import models as smodels

class ActivityManage(umodels.BaseModel):
    """
    活动
    """
    category = models.IntegerField(choices=((0, '商家活动'), (1, '平台活动')), verbose_name='活动分类')
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name='活动标题')
    activity_img = models.ImageField(upload_to='media/active', null=True, blank=True, verbose_name='活动缩略图')
    original_price = models.PositiveIntegerField(verbose_name='原价(单位分)')
    activity_price = models.PositiveIntegerField(verbose_name='活动价(单位分)')
    activity_start_time = models.DateTimeField(verbose_name='活动开始时间')
    activity_end_time = models.DateTimeField(verbose_name='活动结束时间')
    detail = models.TextField()  # 需要使用ueditor
    storemanage=models.ManyToManyField(smodels.StoreManage,verbose_name='商家')

    class Meta:
        db_table = 'activity'
        verbose_name = '活动列表'
        verbose_name_plural = verbose_name
