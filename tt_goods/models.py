# coding=utf-8
from django.db import models
from tinymce.models import HTMLField


# 商品类型
class TypeGoods(models.Model):
    gtype = models.CharField('商品类型', max_length=20)
    isDelete = models.BooleanField('删除', default=False)

    def __str__(self):
        return self.gtype

    class Meta:
        verbose_name = '类型'
        verbose_name_plural = "类型"


class GoodsInfo(models.Model):
    gname = models.CharField('商品名称', max_length=20)
    gpic = models.ImageField('图片', upload_to='static/tt_goods')
    gprice = models.DecimalField('价格', max_digits=5, decimal_places=2)
    gunit = models.CharField('价格单位', max_length=10)
    isDelete = models.BooleanField('删除', default=False)
    gclick = models.IntegerField('点击量', default=0)
    gjianjie = models.CharField('商品简介', max_length=100)
    gkucun = models.IntegerField('库存')
    gcontent = HTMLField('商品介绍')
    gtype = models.ForeignKey(TypeGoods, verbose_name='商品所属分类')

    def __str__(self):
        return self.gname

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'