from django.db import models

# Create your models here.

# 频道信息
class Channel(models.Model):
    name = models.CharField(max_length=100)
    channel_id = models.CharField(max_length=50, unique=True)
    logo_path = models.CharField(max_length=200, blank=True, null=True)  # 新增 logo 字段
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# 节目表信息
class EPG(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    program_date = models.DateField()

    class Meta:
        ordering = ['starttime']

    def __str__(self):
        return f"{self.title} ({self.starttime} - {self.endtime})"
