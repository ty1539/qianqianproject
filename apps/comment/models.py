from django.db import models

# Create your models here.

from users.models import User, BaseModel
from store.models import StoreManage
from order.models import Order


class CommnetManage(BaseModel):
    """
    评论
    """
    store = models.ForeignKey(StoreManage, null=True, blank=True, verbose_name='门店')
    order = models.ForeignKey(Order, null=True, blank=True, verbose_name='订单')
    content = models.TextField(null=True, blank=True, verbose_name='评论内容')
    service = models.IntegerField(choices=((1, '1星'), (2, '2星'), (3, '3星'), (4, '4星'), (5, '5星')),
                                  verbose_name='服务星级评分')
    environment = models.IntegerField(choices=((1, '1星'), (2, '2星'), (3, '3星'), (4, '4星'), (5, '5星')),
                                      verbose_name='环境星级评分')
    comment_img = models.ImageField(upload_to='comment', null=True, blank=True, verbose_name='评论图片')

    class Meta:
        db_table='CommnetManage'
        verbose_name='评论列表'
        verbose_name_plural=verbose_name

