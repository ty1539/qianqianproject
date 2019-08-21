#
# import xadmin
# from users.models import BackLog
# from extra_apps.xadmin.models import Log
# class BackLogAdmin(object):
#     """
#     日志
#     """
#     def link(self, instance):
#         if instance.content_type and instance.object_id and instance.action_flag != 'delete':
#             admin_url = self.get_admin_url('%s_%s_change' % (instance.content_type.app_label, instance.content_type.model),
#                 instance.object_id)
#             return "<a href='%s'>%s</a>" % (admin_url, _('Admin Object'))
#         else:
#             return ''
#     link.short_description = ""
#     link.allow_tags = True
#     link.is_column = False
#
#     list_display = ('action_time', 'user', 'ip_addr', '__str__', 'link')
#     list_filter = ['user', 'action_time']
#     search_fields = ['ip_addr', 'message']
#     model_icon = 'fa fa-cog'
#
# # xadmin.site.unregister(Log)
# xadmin.site.register(BackLog,BackLogAdmin)