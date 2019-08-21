from . import models
import xadmin
class TextmngAdmin(object):

    # model_icon = 'fa fa-amazon'#http://fontawesome.dashgame.com/
    show_bookmarks=False#关闭书签
    list_display = [ 'user_agreement','point_rule','about_us']
    list_editable=[ 'user_agreement','point_rule','about_us']
    list_per_page = 20

xadmin.site.register(models.Textmng, TextmngAdmin)



class StoreApplayAdmin(object):

    # model_icon = 'fa fa-amazon'#http://fontawesome.dashgame.com/
    show_bookmarks=False#关闭书签
    list_display = [ 'store_name','linkman','phone','store_add',]
    search_fields = [ 'store__name',]
    list_editable=[ 'store_name','linkman','phone','store_add',]
    list_per_page = 20

xadmin.site.register(models.StoreApplay, StoreApplayAdmin)



class FeedbackAdmin(object):

    # model_icon = 'fa fa-amazon'#http://fontawesome.dashgame.com/
    show_bookmarks=False#关闭书签
    list_display = [ 'headline','content','check_status','get_user_phone',
                    ]
    search_fields = [ 'user__phone',]
    list_editable=['content']
    list_per_page = 20

    def get_user_phone(self, obj):
        return '%s' % obj.order.user.phone
    get_user_phone.short_description = '用户手机'



xadmin.site.register(models.Feedback, FeedbackAdmin)