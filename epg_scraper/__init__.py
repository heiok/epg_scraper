from __future__ import absolute_import, unicode_literals

# 使 app 在 Django 启动时加载
from .celery import app as celery_app

__all__ = ['celery_app']

