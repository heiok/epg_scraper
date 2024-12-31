import datetime
import pytz
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from epg.models import Channel, EPG
from xml.etree.ElementTree import Element, SubElement, tostring
from django.utils.encoding import smart_str
from django.templatetags.static import static
from django.conf import settings
from .models import Channel
from django.utils.timezone import make_aware, get_current_timezone, utc
from datetime import timedelta

# 用于将 datetime 对象转换为指定时区
def convert_to_timezone(datetime_obj, timezone_str='Asia/Shanghai'):
    tz = pytz.timezone(timezone_str)
    if datetime_obj.tzinfo is None:
        return tz.localize(datetime_obj)  # 转换为指定时区
    else:
        return datetime_obj.astimezone(tz)  # 转为指定时区

def generate_xmltv(request):
    # 获取前6天和后2天的日期范围
    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=6)
    end_date = today + datetime.timedelta(days=2)

    # 获取东八区时区
    timezone = pytz.timezone('Asia/Shanghai')

    # 创建 XMLTV 根元素
    xmltv = Element("tv")

    # 获取所有频道
    channels = Channel.objects.all()

    # 添加频道信息到 XMLTV 中
    for channel in channels:
        channel_elem = SubElement(xmltv, "channel", id=str(channel.channel_id))
        display_name = SubElement(channel_elem, "display-name")
        display_name.text = channel.name

        # 获取该频道在指定日期范围内的节目列表
        epgs = EPG.objects.filter(channel=channel, program_date__range=[start_date, end_date]).order_by("starttime")

        # 添加节目表到 XMLTV 中
        for epg in epgs:
            # 转换开始和结束时间到东八区
            starttime = convert_to_timezone(epg.starttime)
            endtime = convert_to_timezone(epg.endtime)

            program_elem = SubElement(
                xmltv,
                "programme",
                start=starttime.strftime("%Y%m%d%H%M%S +0800"),
                stop=endtime.strftime("%Y%m%d%H%M%S +0800"),
                channel=str(channel.channel_id)
            )
            title_elem = SubElement(program_elem, "title")
            title_elem.text = smart_str(epg.title)

    # 生成 XML 响应
    xml_str = tostring(xmltv, encoding="utf-8", xml_declaration=True)
    response = HttpResponse(xml_str, content_type="application/xml")
    response['Content-Disposition'] = 'attachment; filename="epg.xml"'
    return response

def generate_m3u(request):
    # 获取当前日期，并计算前6天和后2天的日期范围
    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=6)
    end_date = today + datetime.timedelta(days=2)

    # 获取所有频道列表
    channels = Channel.objects.all()

    # M3U 文件的内容
    m3u_content = "#EXTM3U\n"

    # 获取当前主机名（用于构建完整的 logo URL）
    host = request.META['HTTP_HOST']

    # 遍历频道，添加到 M3U 列表中
    for channel in channels:
        # 获取该频道在日期范围内的节目列表
        epgs = EPG.objects.filter(
            channel=channel,
            program_date__range=(start_date, end_date)
        ).order_by('starttime')

        # 构造频道的播放链接（这里假设频道的 URL 格式是标准的 IPTV URL，可以根据需要修改）
        stream_url = f"http://{host}/stream/{channel.channel_id}"

        # 获取频道的 logo 路径，如果没有设置 logo，则使用默认的路径
        if channel.logo_path:
            logo_url = f"http://{host}{static(channel.logo_path)}"  # 构建完整的 logo URL
        else:
            logo_url = f"http://{host}{static('default_logo.png')}"  # 默认 logo

        # 添加频道信息，包括 tvg-logo
        m3u_content += f"#EXTINF:-1 tvg-id=\"{channel.channel_id}\" tvg-name=\"{channel.name}\" tvg-logo=\"{logo_url}\", {channel.name}\n"
        m3u_content += f"{stream_url}\n"

    # 返回 M3U 文件作为响应
    response = HttpResponse(m3u_content, content_type='audio/x-mpegurl')
    response['Content-Disposition'] = 'attachment; filename="channels.m3u"'
    return response

def channel_detail(request, channel_id):
    # 获取频道
    channel = Channel.objects.get(id=channel_id)
    
    # 获取节目表（前七天到后两天的节目信息）
    today = datetime.datetime.now().date()
    start_date = today - datetime.timedelta(days=6)
    end_date = today + datetime.timedelta(days=2)

    epgs = EPG.objects.filter(channel=channel, program_date__range=[start_date, end_date])

    return render(request, 'epg/channel_detail.html', {
        'channel': channel,
        'epgs': epgs
    })

# 首页视图函数：展示频道列表
def homepage(request):
    # 直接定义邮箱地址
    email_address = 'webmaster@example.com'
    channels = Channel.objects.all()
    return render(request, 'index.html', {
        'channels': channels,
        'email_address': email_address,  # 传递邮件地址
    })

def index(request):
    # 直接定义邮箱地址
    email_address = 'webmaster@example.com'

    # 获取频道数据
    channels = Channel.objects.all().order_by('name')

    return render(request, 'index.html', {
        'channels': channels,
        'email_address': email_address,  # 传递邮箱地址
    })

def page_not_found(request, exception):
    return render(request, '404.html', status=404)

def get_channel_epg_json(request, channel_id):
    """
    获取某个频道的节目表 (JSON 格式)
    """
    # 日期范围
    today = datetime.date.today()
    start_date = request.GET.get("start_date", today - datetime.timedelta(days=6))
    end_date = request.GET.get("end_date", today + datetime.timedelta(days=2))

    # 获取频道
    channel = get_object_or_404(Channel, id=channel_id)

    # 获取节目表
    epgs = EPG.objects.filter(channel=channel, program_date__range=[start_date, end_date]).order_by("starttime")
    epg_list = [
        {
            "title": epg.title,
            "starttime": epg.starttime.strftime("%Y-%m-%d %H:%M:%S"),
            "endtime": epg.endtime.strftime("%Y-%m-%d %H:%M:%S"),
        }
        for epg in epgs
    ]

    # 添加 json_dumps_params 参数，确保中文显示正常
    return JsonResponse(
        {"channel": channel.name, "epg": epg_list},
        json_dumps_params={'ensure_ascii': False,'indent': 2}
    )


def get_all_channels_epg_xmltv(request):
    # 获取前6天和后2天的日期范围
    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=6)
    end_date = today + datetime.timedelta(days=2)

    # 获取东八区时区
    timezone = pytz.timezone('Asia/Shanghai')

    # 创建 XMLTV 根元素
    xmltv = Element("tv")

    # 获取所有频道
    channels = Channel.objects.all()

    # 添加频道信息到 XMLTV 中
    for channel in channels:
        channel_elem = SubElement(xmltv, "channel", id=str(channel.channel_id))
        display_name = SubElement(channel_elem, "display-name")
        display_name.text = channel.name

        # 获取该频道在指定日期范围内的节目列表
        epgs = EPG.objects.filter(channel=channel, program_date__range=[start_date, end_date]).order_by("starttime")

        # 添加节目表到 XMLTV 中
        for epg in epgs:
            # 转换开始和结束时间到东八区
            starttime = convert_to_timezone(epg.starttime)
            endtime = convert_to_timezone(epg.endtime)

            program_elem = SubElement(
                xmltv,
                "programme",
                start=starttime.strftime("%Y%m%d%H%M%S +0800"),
                stop=endtime.strftime("%Y%m%d%H%M%S +0800"),
                channel=str(channel.channel_id)
            )
            title_elem = SubElement(program_elem, "title")
            title_elem.text = smart_str(epg.title)

    # 生成 XML 响应
    xml_str = tostring(xmltv, encoding="utf-8", xml_declaration=True)
    response = HttpResponse(xml_str, content_type="application/xml")
    response['Content-Disposition'] = 'inline; filename="epg_all_channels.xml"'  # 改为返回所有频道的 XML
    return response


def view_xmltv(request):
    # 定义中国标准时间时区
    cst = pytz.timezone("Asia/Shanghai")

    # 获取前6天和后2天的日期范围
    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=6)
    end_date = today + datetime.timedelta(days=2)

    # 创建 XMLTV 根元素
    xmltv = Element("tv")

    # 获取所有频道
    channels = Channel.objects.all()

    for channel in channels:
        # 创建频道节点
        channel_elem = SubElement(xmltv, "channel", id=str(channel.channel_id))
        display_name = SubElement(channel_elem, "display-name")
        display_name.text = channel.name

        # 获取该频道在指定日期范围内的节目列表
        epgs = EPG.objects.filter(
            channel=channel, program_date__range=[start_date, end_date]
        ).order_by("starttime")

        for epg in epgs:
            # 检查 starttime 和 endtime 是否有效
            if not epg.starttime or not epg.endtime:
                continue  # 跳过无效的节目数据

            try:
                # 确保时间以中国标准时间显示
                if epg.starttime.tzinfo is None:  # 天真的时间
                    start_cst = make_aware(epg.starttime, cst)
                else:  # 已有时区信息
                    start_cst = epg.starttime.astimezone(cst)

                if epg.endtime.tzinfo is None:  # 天真的时间
                    end_cst = make_aware(epg.endtime, cst)
                else:  # 已有时区信息
                    end_cst = epg.endtime.astimezone(cst)

                # 转换为 +0800 格式的字符串
                start_str = start_cst.strftime("%Y%m%d%H%M%S +0800")
                end_str = end_cst.strftime("%Y%m%d%H%M%S +0800")

                # 创建节目节点
                program_elem = SubElement(
                    xmltv,
                    "programme",
                    start=start_str,
                    stop=end_str,
                    channel=str(channel.channel_id),
                )
                title_elem = SubElement(program_elem, "title")
                title_elem.text = smart_str(epg.title)
            except Exception as e:
                # 日志记录并跳过该节目
                print(f"Error processing EPG entry {epg.id}: {e}")
                continue

    # 生成 XML 响应
    xml_str = tostring(xmltv, encoding="utf-8", xml_declaration=True)
    return HttpResponse(xml_str, content_type="application/xml")
