#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/16 18:06
# @Author  : Lijinjin
# @Site    : 
# @File    : models.py
# @Software: PyCharm
from django.db import models
from django.utils import timezone


class User(models.Model):
    # 用户表
    gender = (
        ('male', '男'),
        ('female', '女'),
    )
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'