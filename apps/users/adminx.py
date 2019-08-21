import xadmin
from xadmin import views

from . import models
from django.utils.html import format_html
from django.contrib.auth import models as amodels
from django.contrib.auth import get_user_model
class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True #显示更多主题

xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "钳钳后台管理系统"  # 设置站点标题
    site_footer = "钳钳科技有限公司"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠

    # def get_site_menu(self):
    #     from discount_coupon.models import Discount
    #     from store.models import StoreManage,Store2User,UserWater
    #     from order.models import Order
    #     from points_mall.models import Shopping,LuckyShopping,TaskManage,PointOrder,LogisticsCompany
    #     from activity.models import ActivityManage
    #     from comment.models import CommnetManage
    #     from finance.models import OverApply,IsOverApply,UserWallet,StoreWallet
    #     from textmanager.models import Textmng,StoreApplay,Feedback
    #     from advertisement.models import Adver
    #     # from extra_apps.xadmin.models import Log
    #
    #     for model, model_admin in self.admin_site._registry.items():
    #
    #         return (
    #             {'title': '主页管理','perm': self.get_model_perm(model, 'view'), 'menus': (
    #
    #                 {'title': '主页', 'url': self.get_model_url(model, 'changelist')},#主页
    #             )},
    #
    #             # {'title': '用户管理','perm': self.get_model_perm(model, 'view'),  'menus': (
    #             #     {'title': '用户列表', 'url': self.get_model_url(models.User, 'changelist')},#用户管理
    #             # )},
    #
    #             {'title': '优惠券管理','perm': self.get_model_perm(model, 'view'),  'menus': (
    #                 {'title': '优惠券列表', 'url': self.get_model_url(Discount, 'changelist')},#优惠券管理
    #             )},
    #
    #             {'title': '门店管理','perm': self.get_model_perm(model, 'view'),   'menus': (
    #                 {'title': '门店列表', 'url': self.get_model_url(StoreManage, 'changelist')},  # 门店管理
    #             )},
    #
    #             {'title': '订单管理','perm': self.get_model_perm(model, 'view'),  'menus': (
    #                 {'title': '订单列表', 'url': self.get_model_url(Order, 'changelist')},  # 订单管理
    #             )},
    #
    #             {'title': '积分商城','perm': self.get_model_perm(model, 'view'),  'menus': (
    #                 {'title': '商品列表', 'url': self.get_model_url(Shopping, 'changelist')},  # 积分商城
    #                 {'title': '抽奖商品列表', 'url': self.get_model_url(LuckyShopping, 'changelist')},
    #                 {'title': '任务列表', 'url': self.get_model_url(TaskManage, 'changelist')},
    #                 {'title': '积分商城订单', 'url': self.get_model_url(PointOrder, 'changelist')},
    #                 {'title': '物流公司列表', 'url': self.get_model_url(LogisticsCompany, 'changelist')},
    #             )},
    #
    #             {'title': '活动管理','perm': self.get_model_perm(model, 'view'),   'menus': (
    #                 {'title': '活动列表', 'url': self.get_model_url(ActivityManage, 'changelist')},  # 订单管理
    #             )},
    #
    #             {'title': '文本管理', 'perm': self.get_model_perm(model, 'view'), 'menus': (
    #                 {'title': '文本列表', 'url': self.get_model_url(Textmng, 'changelist')},
    #                 {'title': '商家申请列表', 'url': self.get_model_url(StoreApplay, 'changelist')},
    #                 {'title': '反馈建议列表', 'url': self.get_model_url(Feedback, 'changelist')},
    #             )},
    #             {'title': '广告管理', 'perm': self.get_model_perm(model, 'view'), 'menus': (
    #                 {'title': '广告列表', 'url': self.get_model_url(Adver, 'changelist')},
    #             )},
    #
    #             {'title': '评价管理', 'perm': self.get_model_perm(model, 'view'), 'menus': (
    #                 {'title': '评价列表', 'url': self.get_model_url(CommnetManage, 'changelist')},
    #             )},
    #
    #             {'title': '财务管理', 'perm': self.get_model_perm(model, 'view'), 'menus': (
    #                 {'title': '申请提现列表', 'url': self.get_model_url(OverApply, 'changelist')},
    #                 {'title': '已提现列表', 'url': self.get_model_url(IsOverApply, 'changelist')},
    #                 {'title': '用户钱包', 'url': self.get_model_url(UserWallet, 'changelist')},
    #                 {'title': '商家钱包', 'url': self.get_model_url(StoreWallet, 'changelist')},
    #                 {'title': '商家钱包流水', 'url': self.get_model_url(Store2User, 'changelist')},
    #                 {'title': '用户钱包流水', 'url': self.get_model_url(UserWater, 'changelist')},
    #             )},
    #
    #             {'title': '管理员', 'perm': self.get_model_perm(model, 'view'), 'menus': (
    #                 {'title': '管理员列表', 'url': self.get_model_url(models.SysUser, 'changelist')},
    #             )},
    #
    #             # {'title': '日志管理', 'perm': self.get_model_perm(model, 'view'), 'menus': (
    #             #     {'title': '日志列表', 'url': self.get_model_url(Log, 'changelist')},
    #             # )},
    #
    #         )

xadmin.site.register(views.CommAdminView, GlobalSettings)


class PointInlines(object):
    model=models.PointsRecord
    extra=0


class UserAdmin(object):
    list_per_page = 10
    list_export = ('xls',)
    list_export_fields = ('id', "name", "phone", "create_time")#暂时无用
    show_bookmarks=False#关闭书签
    list_display = [ 'id','name', 'preview','phone','balance','get_discount','all_point']

    def preview(self, obj):
        return '<img src="/media/%s" height="50" width="50" />' % (obj.head_img)
    preview.allow_tags = True
    preview.short_description = "用户头像"

    def get_discount(self, obj):
        discount_queryset = obj.discount_set.all()
        if discount_queryset.first():
            # return str(["优惠券名称:%s" % (i.discount_name) for i in discount_queryset])
            return format_html(
                '<span style="color:red;">{}</span>',
                ','.join([i.discount_name for i in discount_queryset],))
        else:
            return ''
    get_discount.short_description = '优惠券'
    # inlines=[PointInlines]
    # def get_point(self,obj):#获取用户积分
    #     point=obj.pointsrecord.all()
    #     if point.first():
    #         return format_html(
    #             '<span style="color:red;">{}</span>',
    #             str(point.last().point
    #         ))
    #     else:
    #         return ''


    # get_point.short_description = '用户积分'

    search_fields = [ 'name',]
    list_editable=['balance','integral']


xadmin.site.register(models.User,UserAdmin)

from django.contrib.auth.models import AbstractUser, Group
class SysUserAdmin(object):
    list_display = ['username', 'password','email', 'date_joined', 'is_staff','get_zu']
    search_fields = ['username', 'email', 'is_staff']
    list_filter = ['username', 'email', 'is_staff']

    def save_models(self):
        # 重载密码加密
        obj = self.new_obj
        if not obj.is_superuser:
            if obj.save_num == 0:
                obj.set_password(obj.password)
                obj.save_num+=1
                obj.save()


    def get_zu(self, obj):
        if obj.is_superuser:

            return format_html(
                '<span style="color:red;">{}</span>',
                '超级管理员' )
        zu=obj.groups.all()
        if zu.first():
            return format_html(
                '<span style="color:red;">{}</span>',
                [i.name for i in zu] )
        else:
            return '不属于任何权限组'

    get_zu.short_description = '所属权限组'


xadmin.site.unregister(get_user_model())
xadmin.site.register(models.SysUser,SysUserAdmin)




class PonitAdmin(object):
    list_per_page = 20
    show_bookmarks=False#关闭书签
    list_display = [ 'id','user', 'point','used','expire']
    list_editable = ['user']

xadmin.site.register(models.PointsRecord,PonitAdmin)



