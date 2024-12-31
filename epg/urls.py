from django.urls import path
from epg.views import index, generate_xmltv
from . import views
from django.conf.urls import handler404
from epg import views

handler404 = 'epg.views.page_not_found'  # 替换为你自己定义的视图函数

urlpatterns = [
    path('', index, name='index'),  # 首页
    path('xmltv/', generate_xmltv, name='generate_xmltv'),  # XMLTV 文件导出
    path('m3u/', views.generate_m3u, name='generate_m3u'),  # M3U 链接
    path('channel/<int:channel_id>/', views.channel_detail, name='channel_detail'),  # 频道详情页
    path('api/channel/<int:channel_id>/epg/json/', views.get_channel_epg_json, name='channel_epg_json'),
    path('api/all_channels/epg/xmltv/', views.get_all_channels_epg_xmltv, name='all_channels_epg_xmltv'),
    path('xmltv/view_epg.xml', views.view_xmltv, name='view_xmltv'),

]

