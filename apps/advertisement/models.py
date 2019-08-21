from django.db import models

# Create your models here.

from users.models import BaseModel, User


class Adver(BaseModel):
    """
    广告列表
    """
    adver_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='广告名称')
    adver_img = models.ImageField(upload_to='adver', null=True, blank=True, verbose_name='广告图片')
    adver_img_url = models.CharField(max_length=200, blank=True, null=True, verbose_name='广告图片超链接')

    class Meta:
        db_table = 'Adver'
        verbose_name = '广告列表'
        verbose_name_plural = verbose_name
