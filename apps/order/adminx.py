import xadmin
from xadmin import views

from . import models
from users import models as umodels
# class OrderAdmin(object):
#     model_icon = 'fa file-text-o'#http://fontawesome.dashgame.com/
#     show_bookmarks=False#关闭书签
#     list_display = [ 'order_sn','trade_no', 'total_money','handel_money','user_real_money','store_real_money',
#                      'pay_type','pay_status','order_status','order_type',
#                      ]




    # search_fields = [ 'user__name']


@xadmin.sites.register(models.Order)
class OrderAdmin(object):
    list_per_page = 20
    list_display = ['order_sn', 'trade_no', 'total_money', 'handel_money', 'user_real_money', 'store_real_money',
                    'pay_type', 'pay_status', 'order_status', 'order_type','get_store_name','get_user_name'
                    ]

    def get_store_name(self, obj):
        return '%s' % obj.storemanage.store_name
    get_store_name.short_description = '商店名称'

    def get_user_name(self, obj):
        return '%s' % obj.user.name
    get_user_name.short_description = '用户名称'

    search_fields = ['storemanage__store_name', 'user__name' ]

    list_filter = ['create_time',]



