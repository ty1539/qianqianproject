import xadmin
from xadmin import views

from . import models


class OverApplyAdmin(object):
    #提现申请
    # model_icon = 'fa fa-amazon'#http://fontawesome.dashgame.com/
    show_bookmarks = False  # 关闭书签
    list_display = ['store', 'withdraw_money', 'get_cardholder',
                    'get_bank_num', 'get_belong_bank', 'create_time', 'check_status']
    search_fields = ['store__name','store__area ']
    list_editable = ['check_status']
    list_per_page = 20
    date_hierarchy = 'create_time'
    ordering = ['-create_time',]
    list_filter = ['store__area']

    def get_cardholder(self, obj):
        return '%s' % obj.store.cardholder

    get_cardholder.short_description = '持卡人'

    def get_bank_num(self, obj):
        return '%s' % obj.store.bank_num

    get_bank_num.short_description = '银行卡号'

    def get_belong_bank(self, obj):
        return '%s' % obj.store.belong_bank

    get_belong_bank.short_description = '所属银行'

    def queryset(self):
        qs = super(OverApplyAdmin, self).queryset()
        qs = qs.filter(check_status=1)  # 提现还未通过审核
        return qs


xadmin.site.register(models.OverApply, OverApplyAdmin)


class IsOverApplyAdmin(object):
    #已提现
    # model_icon = 'fa fa-amazon'#http://fontawesome.dashgame.com/
    show_bookmarks = False  # 关闭书签
    list_display = ['store', 'withdraw_money', 'get_cardholder',
                    'get_bank_num', 'get_belong_bank', 'create_time', 'check_status']
    search_fields = ['store__name', 'store__area ']
    list_editable = ['check_status']
    list_per_page = 20
    date_hierarchy = 'create_time'
    ordering = ['-create_time', ]
    list_filter = ['store__area']

    def get_cardholder(self, obj):
        return '%s' % obj.store.cardholder

    get_cardholder.short_description = '持卡人'

    def get_bank_num(self, obj):
        return '%s' % obj.store.bank_num

    get_bank_num.short_description = '银行卡号'

    def get_belong_bank(self, obj):
        return '%s' % obj.store.belong_bank

    get_belong_bank.short_description = '所属银行'

    def queryset(self):
        qs = super(IsOverApplyAdmin, self).queryset()
        qs = qs.filter(check_status=0)  # 提现已通过审核
        return qs


xadmin.site.register(models.IsOverApply, IsOverApplyAdmin)


class StoreWalletAdmin(object):
    #商家钱包
    # model_icon = 'fa fa-amazon'#http://fontawesome.dashgame.com/
    show_bookmarks = False  # 关闭书签
    list_display = ['store_name', 'balance', 'get_is_over_apply','all_service_charge','phone','linkman']
    search_fields = ['store__name', ]
    list_per_page = 20
    list_editable = ['balance']
    # readonly_fields=['check_status']
    date_hierarchy = 'create_time'

    def get_is_over_apply(self, obj):
        qset=obj.overapply_set.all().reverse()
        if qset:
            if len(qset)>10:
                q=qset[:10]
            else:
                q=qset

            return '%s' % ([(i.create_time.strftime('%Y-%m-%d %H:%M'),i.get_check_status_display(),'金额:%s'%(i.withdraw_money)) for i in q])

        else:
            return ''

    get_is_over_apply.short_description = '历史已提现'

xadmin.site.register(models.StoreWallet, StoreWalletAdmin)



class UserWalletAdmin(object):
    #用户钱包
    # model_icon = 'fa fa-amazon'#http://fontawesome.dashgame.com/
    show_bookmarks = False  # 关闭书签
    list_display = ['name', 'balance', 'phone','all_point']
    search_fields = ['name', 'balance']
    list_per_page = 20
    list_editable = ['balance',]
    # readonly_fields=['check_status']
    date_hierarchy = 'create_time'

xadmin.site.register(models.UserWallet, UserWalletAdmin)



from store.models import Store2User
class Store2UserAdmin(object):
    #商家钱包流水
    # model_icon = 'fa fa-amazon'#http://fontawesome.dashgame.com/
    show_bookmarks = False  # 关闭书签
    list_display = ['store', 'store_water_num', 'user',
                    'store_money', 'store_source', 'create_time']
    search_fields = ['store__name', 'user__name ']
    list_per_page = 20

xadmin.site.register(Store2User, Store2UserAdmin)


from store.models import UserWater
class UserWaterAdmin(object):
    #用户钱包流水
    # model_icon = 'fa fa-amazon'#http://fontawesome.dashgame.com/
    show_bookmarks = False  # 关闭书签
    list_display = ['user', 'user_water_num', 'store',
                    'user_money', 'user_source', 'create_time']
    search_fields = ['store__name', 'user__name ']

    list_per_page = 20

xadmin.site.register(UserWater, UserWaterAdmin)