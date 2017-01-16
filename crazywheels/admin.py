from django.contrib import admin

from .models import MessageModel


# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    pass
admin.site.register(MessageModel, MessageAdmin)
