"""
https://tool.oschina.net/encrypt?type=3
"""
from django.db import models


class Node(models.Model):
    name = models.CharField("名称", max_length=64, unique=True)
    link = models.CharField("配置链接",max_length=1024, unique=True)
    updated = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '节点'
        verbose_name_plural = verbose_name
        ordering = ['-updated']
        app_label = 'proxy'

    def __str__(self):
        return self.name