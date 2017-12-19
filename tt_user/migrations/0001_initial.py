# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=40)),
                ('uemail', models.CharField(max_length=30)),
                ('ushou', models.CharField(default='', max_length=40)),
                ('uaddr', models.CharField(default='', max_length=100)),
                ('upostcode', models.CharField(default='', max_length=6)),
                ('uphone', models.CharField(default='', max_length=11)),
            ],
        ),
    ]
