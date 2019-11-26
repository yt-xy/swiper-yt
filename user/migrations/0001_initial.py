# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-26 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenum', models.CharField(max_length=15, unique=True, verbose_name='手机号')),
                ('nickname', models.CharField(max_length=20, verbose_name='昵称')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], max_length=6, verbose_name='性别')),
                ('birthday', models.DateField(default='1990-01-01', verbose_name='生日')),
                ('location', models.CharField(choices=[('北京', '北京'), ('上海', '上海'), ('深圳', '深圳'), ('郑州', '郑州'), ('西安', '西安'), ('成都', '成都'), ('沈阳', '沈阳')], max_length=15, verbose_name='常居地')),
                ('avatar', models.ImageField(max_length=256, upload_to='', verbose_name='个人形象')),
            ],
        ),
    ]
