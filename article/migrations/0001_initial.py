# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-10 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(help_text='カテゴリを判定したい記事URLを入力してください', max_length=255, verbose_name='記事URL')),
            ],
        ),
    ]
