from . import models
import xadmin
class AdverAdmin(object):

    # model_icon = 'fa fa-amazon'#http://fontawesome.dashgame.com/
    show_bookmarks=False#关闭书签
    list_display = [ 'adver_name','preview','adver_img_url',]

    list_editable=[ 'adver_name','adver_img_url',]
    list_per_page = 20

    def preview(self, obj):
        return '<img src="/media/%s" height="50" width="50" />' % (obj.adver_img)


    preview.allow_tags = True
    preview.short_description = "广告图片"


xadmin.site.register(models.Adver, AdverAdmin)