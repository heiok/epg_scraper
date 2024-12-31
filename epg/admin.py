from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Channel, EPG

# 注册 Channel 模型
@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'channel_id', 'updated_at')
    search_fields = ('name', 'channel_id')

# 注册 EPG 模型
@admin.register(EPG)
class EPGAdmin(admin.ModelAdmin):
    list_display = ('id', 'channel', 'title', 'starttime', 'endtime', 'program_date')
    search_fields = ('title',)
    list_filter = ('channel', 'program_date')

