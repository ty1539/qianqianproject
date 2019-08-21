import xadmin
from xadmin import views

from . import models

class SystemAdmin(object):


    list_per_page = 20
    show_bookmarks=False#关闭书签
    list_display = [ 'title','keywords', 'description','logo','company_name','wechat',
                     'email','address','beiancode','phone','create_time']
    search_fields = [ 'company_name',]
    list_editable=[ 'title','keywords', 'description','logo','company_name','wechat',
                     'email','address','beiancode','phone','create_time']

xadmin.site.register(models.System,SystemAdmin)


class RechargeAdmin(object):
    list_per_page = 20
    show_bookmarks=False#关闭书签
    list_display = [ 'system','money','create_time']
    search_fields = [ 'company_name',]
    list_editable=[ 'money',]

xadmin.site.register(models.Recharge,RechargeAdmin)


class QrcodeAdmin(object):

    """
    二维码设置
    """
    list_per_page = 20
    show_bookmarks=False#关闭书签
    list_display = [ 'qrcode_day',]
    list_editable=[ 'qrcode_day',]

xadmin.site.register(models.Qrcode,QrcodeAdmin)


class SetPointAdmin(object):
    """
    积分设置
    """
    list_per_page = 20
    show_bookmarks = False  # 关闭书签
    list_display = ['jifen_chongzhi','jifen_max' ]
    list_editable = ['jifen_chongzhi','jifen_max' ]
xadmin.site.register(models.SetPoint, SetPointAdmin)