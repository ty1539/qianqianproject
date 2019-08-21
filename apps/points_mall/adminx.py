import xadmin
from xadmin import views

from . import models


class ShoppingAdmin(object):
    """
    商品
    """
    list_per_page = 20
    show_bookmarks=False#关闭书签
    list_display = [ 'shopping_type','name', 'need_point','color','size','weight','repertory','detail',]
    style_fields = {"detail": "ueditor"}
    search_fields = [ 'name',]
    list_editable=['name','need_point']

xadmin.site.register(models.Shopping,ShoppingAdmin)


class LuckyShoppingAdmin(object):
    """
    抽奖商品
    """
    list_per_page = 20
    # model_icon = 'fa fa-circle'#http://fontawesome.dashgame.com/
    show_bookmarks=False#关闭书签
    list_display = [ 'get_shopping_name','luckyshopping_type',]
    search_fields = [ 'shopping__name',]
    list_editable=['shopping__name','shopping__need_point']

    def get_shopping_name(self, obj):
        return '%s' % obj.shopping.name
    get_shopping_name.short_description = '商品名称'

    # def get_shopping_need_point(self, obj):
    #     return '%s' % obj.shopping.need_point
    # get_shopping_need_point.short_description = '商品兑换需要的积分'
    #
    # def get_shopping_color(self, obj):
    #     return '%s' % obj.shopping.color
    # get_shopping_color.short_description = '颜色'
    #
    # def get_shopping_weight(self, obj):
    #     return '%s' % obj.shopping.weight
    # get_shopping_weight.short_description = '重量'
    #
    # def get_shopping_repertory(self, obj):
    #     return '%s' % obj.shopping.repertory
    # get_shopping_repertory.short_description = '库存'
    #
    # def get_shopping_detail(self, obj):
    #     return '%s' % obj.shopping.detail
    # get_shopping_detail.short_description = '商品详情'
    #
    # def get_shopping_size(self, obj):
    #     return '%s' % obj.shopping.size
    # get_shopping_size.short_description = '尺寸'


xadmin.site.register(models.LuckyShopping,LuckyShoppingAdmin)


class TaskManageAdmin(object):
    list_per_page = 20
    show_bookmarks=False#关闭书签
    list_display = [ 'one_time_point','all_month_point', 'invite_point','consume_point','recharge_point','share_point','comment_point',]
    list_editable=[ 'one_time_point','all_month_point', 'invite_point','consume_point','recharge_point','share_point','comment_point',]

xadmin.site.register(models.TaskManage,TaskManageAdmin)


class PointOrderAdmin(object):
    list_per_page = 20

    # model_icon = 'fa fa-amazon'#http://fontawesome.dashgame.com/
    show_bookmarks=False#关闭书签
    list_display = [ 'get_shopping_name','get_shopping_type','luckyshopping', 'get_user_name','get_user_phone',
                     'order_status','get_logistics_company_name','tracking_number',]
    search_fields = [ 'shopping__name',]
    list_editable=['shopping__name']

    def get_shopping_name(self, obj):
        return '%s' % obj.shopping.name
    get_shopping_name.short_description = '商品名称'

    def get_shopping_type(self, obj):
        return '%s' % obj.shopping.shopping_type
    get_shopping_type.short_description = '商品类型'

    def get_user_name(self, obj):
        return '%s' % obj.user.name
    get_user_name.short_description = '用户名称'

    def get_user_phone(self, obj):
        return '%s' % obj.user.phone
    get_user_phone.short_description = '用户电话'

    def get_logistics_company_name(self, obj):
        return '%s' % obj.logistics_company.name
    get_logistics_company_name.short_description = '物流公司名称'

xadmin.site.register(models.PointOrder, PointOrderAdmin)

class LogisticsCompanyAdmin(object):
    list_per_page = 20
    show_bookmarks=False#关闭书签
    list_display = ['name']
    search_fields = ['name',]
    list_editable=['name']

xadmin.site.register(models.LogisticsCompany, LogisticsCompanyAdmin)