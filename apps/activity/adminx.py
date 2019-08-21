import xadmin
from xadmin import views

from . import models



class ActivityManageAdmin(object):
    list_per_page = 20

    show_bookmarks=False#关闭书签
    list_display = [ 'category','title', 'activity_img','original_price','activity_price','activity_start_time',
                     'activity_end_time','detail'
                     ]
    search_fields = [ 'name','storemanage__store_name']


xadmin.site.register(models.ActivityManage,ActivityManageAdmin)