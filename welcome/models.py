# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class PageView(models.Model):
    hostname = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)

ITEM_LIST = (u'001---佛号或咒语---',u'002 阿弥陀佛',u'005 百字明',u'010 地藏菩萨',u'015 度母心咒',u'020 观音心咒',
     u'025 金刚镢心咒',u'030 金刚萨埵心咒',u'035 九本尊心咒',u'040 楞严咒',u'045 莲师心咒',u'050 往生咒',
     u'055 文殊心咒',u'060具光佛母心咒',u'300---经论或祈祷文---',u'301 八吉祥颂',u'310 大自在祈祷文',
     u'315 二十一度母赞',u'320 法王如意宝祈祷文',u'325 金刚经',u'330 莲师七句',u'335 普获悉地祈祷文',
     u'340 普贤行愿品',u'350 心经',u'500---其他---',u'510 供灯' )


class SignInfo(models.Model):
    ITEM_CHOICE = [ (str(i),v) for i,v in enumerate(ITEM_LIST) ]
    name = models.CharField(max_length=100, verbose_name=u'昵称'.encode('utf8'))
    date = models.DateField(verbose_name=u'日期'.encode('utf8'))
    item = models.CharField(choices = ITEM_CHOICE, verbose_name=u'经咒'.encode('utf8'), max_length=100)
    number = models.IntegerField(verbose_name=u'数量'.encode('utf8'))