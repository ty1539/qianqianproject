from . import models
import xadmin
class CommnetManageAdmin(object):

    # model_icon = 'fa fa-amazon'#http://fontawesome.dashgame.com/
    show_bookmarks=False#关闭书签
    list_display = [ 'store','order','get_user_name','get_user_phone',
                     'content','service','environment','preview','create_time']
    search_fields = [ 'store__name',]
    list_editable=['content']
    list_per_page = 20

    def get_user_name(self, obj):
        return '%s' % obj.order.user.name
    get_user_name.short_description = '用户姓名'

    def get_user_phone(self, obj):
        return '%s' % obj.order.user.phone
    get_user_phone.short_description = '用户手机'

    def preview(self, obj):
        return '<img src="/media/%s" height="50" width="50" />' % (obj.comment_img)


    preview.allow_tags = True
    preview.short_description = "评论图片"


xadmin.site.register(models.CommnetManage, CommnetManageAdmin)