# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('gname', models.CharField(max_length=20)),
                ('gpic', models.ImageField(upload_to='tt_goods')),
                ('gprice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('gunit', models.CharField(max_length=10)),
                ('isDelete', models.BooleanField(default=False)),
                ('gclick', models.IntegerField()),
                ('gjianjie', models.CharField(max_length=100)),
                ('gkucun', models.IntegerField()),
                ('gcontent', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeGoods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('gtype', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(to='tt_goods.TypeGoods'),
        ),
    ]
