import xadmin
from xadmin import views

from . import models

from django.utils.html import format_html

class DiscountAdmin(object):
    list_per_page = 20
    show_bookmarks=False#关闭书签
    list_display = [ 'user','discount_name','discount_num','get_user_phone', 'discount_money','validity_time',
                     'discount_status','create_time']

    list_export = ('xls',)
    list_export_fields = ('discount_money',)

    def get_user_phone(self,obj):
        return '%s'%(obj.user.phone)

    get_user_phone.short_description='用户手机号'
    search_fields = [ 'discount_name',]
    list_editable=['discount_name',]




xadmin.site.register(models.Discount,DiscountAdmin)