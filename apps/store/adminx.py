import xadmin
from xadmin import views

from . import models

class StoreAdmin(object):
    list_per_page = 20
    show_bookmarks=False#关闭书签
    list_display = [ 'store_name','logo', 'up_five_price','low_five_price','service_content','graded',
                     'area','office_hours','closing_time','audit_status','commission_rate','phone','create_time']
    search_fields = [ 'store_name','audit_status']
    list_editable=['store_name','up_five_price','up_five_price']

xadmin.site.register(models.StoreManage,StoreAdmin)