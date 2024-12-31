import sys
import os
import django

# 添加项目根目录到 sys.path 中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# 设置 Django 环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "epg_scraper.settings")  # 替换为你的 Django 项目名
django.setup()

import datetime
import requests
import warnings
from bs4 import BeautifulSoup as bs
from epg.models import Channel, EPG
from django.db import IntegrityError

# 定义请求头，模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

# 忽略 XMLParsedAsHTMLWarning
warnings.filterwarnings('ignore')

# 获取广东电视台频道列表
def get_channels_gdtv():
    url = 'http://epg.gdtv.cn/f/1.xml'  # 获取广东电视台频道列表的XML文件
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    soup = bs(res.text, 'lxml')
    contents = soup.select('channel')
    channels = []

    # 遍历频道内容并检查是否存在
    for content in contents:
        channel_id = content.attrs['id']
        name = content.ctitle.text.strip()  # 使用 strip() 清理可能的空格和换行

        # 确保频道唯一，避免重复添加
        existing_channels = Channel.objects.filter(channel_id=channel_id)
        if existing_channels.exists():
            print(f"频道 {name} 已存在于数据库。")
        else:
            Channel.objects.create(name=name, channel_id=channel_id)
            print(f"频道 {name} 已添加到数据库。")

        channels.append(existing_channels.first() if existing_channels.exists() else Channel.objects.get(channel_id=channel_id))

    return channels

# 处理节目标题中的 HTML 实体和标签
def clean_html(text):
    # 将 HTML 实体转换为普通字符（例如 &amp; -> &）
    text = bs(text, "html.parser").get_text()

    # 替换 <br /> 标签为换行符
    text = text.replace('<br />', '\n').replace('<br>', '\n')
    
    return text.strip()

# 获取指定日期范围内的节目表
def get_epgs_gdtv(channel, start_date, end_date):
    epgs = []
    success = 1
    try:
        # 循环抓取指定日期范围内的节目
        current_date = start_date
        while current_date <= end_date:
            url = f'http://epg.gdtv.cn/f/{channel.channel_id}/{current_date.strftime("%Y-%m-%d")}.xml'
            res = requests.get(url, headers=headers, timeout=8)
            res.encoding = 'utf-8'
            soup = bs(res.text, 'lxml-xml')
            epgs_contents = soup.select('content')

            # 解析并保存节目数据
            for epga in epgs_contents:
                starttime = datetime.datetime.fromtimestamp(int(epga.attrs['time1']))
                endtime = datetime.datetime.fromtimestamp(int(epga.attrs['time2']))
                title = clean_html(epga.get_text())  # 使用清理函数

                # 检查数据库中是否已经存在相同的节目
                if not EPG.objects.filter(channel=channel, starttime=starttime, title=title).exists():
                    try:
                        # 如果不存在，则创建新的节目记录
                        EPG.objects.create(
                            channel=channel,
                            title=title,
                            starttime=starttime,
                            endtime=endtime,
                            program_date=current_date
                        )
                        print(f"新增节目: {title} ({starttime} - {endtime})")
                    except IntegrityError:
                        print(f"插入节目时发生错误: {title}")

            current_date += datetime.timedelta(days=1)  # 增加一天

        print(f"成功抓取 {channel.name} 的节目表。")
    except Exception as e:
        print(f"抓取 {channel.name} 的节目表失败: {e}")
        success = 0

    return success, epgs

# 获取前六天到后两天的节目表
def fetch_all_channels_and_epgs():
    today = datetime.datetime.now().date()
    start_date = today - datetime.timedelta(days=6)  # 六天前
    end_date = today + datetime.timedelta(days=2)  # 两天后

    channels = get_channels_gdtv()  # 获取并确保频道存在
    for channel in channels:
        get_epgs_gdtv(channel, start_date, end_date)  # 抓取并保存节目信息

# 执行抓取
if __name__ == "__main__":
    fetch_all_channels_and_epgs()

