from celery import shared_task
from epg.spiders.gdtv import fetch_all_channels_and_epgs

@shared_task
def update_gdtv_epg():
    """
    Celery 定时任务：更新广东电视台节目信息
    """
    fetch_all_channels_and_epgs()

