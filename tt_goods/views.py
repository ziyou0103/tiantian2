from django.shortcuts import render
from tt_goods.models import TypeGoods, GoodsInfo
from django.core.paginator import Paginator


def index(request):
    type_list = TypeGoods.objects.all()
    type0 = type_list[0].goodsinfo_set.order_by('-id')[0:4]
    type01 = type_list[0].goodsinfo_set.order_by('-gclick')[0:3]
    type1 = type_list[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = type_list[1].goodsinfo_set.order_by('-gclick')[0:3]
    type2 = type_list[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = type_list[2].goodsinfo_set.order_by('-gclick')[0:3]
    type3 = type_list[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = type_list[3].goodsinfo_set.order_by('-gclick')[0:3]
    type4 = type_list[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = type_list[4].goodsinfo_set.order_by('-gclick')[0:3]
    type5= type_list[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = type_list[5].goodsinfo_set.order_by('-gclick')[0:3]
    context = {
        'title': '首页',
        'type0': type0, 'type01': type01, 'good1': type_list[0],
        'type1': type1, 'type11': type11, 'good2': type_list[1],
        'type2': type2, 'type21': type21, 'good3': type_list[2],
        'type3': type3, 'type31': type31, 'good4': type_list[3],
        'type4': type4, 'type41': type41, 'good5': type_list[4],
        'type5': type5, 'type51': type51, 'good6': type_list[5],
    }
    return render(request, 'tt_goods/index.html', context)


def list(request, typeid, sortid, pageid):
    '''
    :param type: 商品所属分类id
    :param sort: 商品排序：１表示按商品id排,２表示价格倒序, 3点击量倒序
    :param page: 商品所处页面id
    '''
    # 获取所有分类
    type_list = TypeGoods.objects.all()
    type0 = type_list[0]
    type1 = type_list[1]
    type2 = type_list[2]
    type3 = type_list[3]
    type4 = type_list[4]
    type5 = type_list[5]
    # 根据类型id获得商品所属分类
    type_goods = TypeGoods.objects.get(pk=int(typeid))
    new_goods = type_goods.goodsinfo_set.order_by('-id')[0:2]
    if sortid == '1':
        goods_list = type_goods.goodsinfo_set.all()
    elif sortid == '2':
        goods_list = type_goods.goodsinfo_set.order_by('-gprice')
    elif sortid == '3':
        goods_list = type_goods.goodsinfo_set.order_by('-gclick')
    # 分页
    paginator = Paginator(goods_list, 10)
    page = paginator.page(int(pageid))
    context = {
        'title': '商品列表', 'typeid': typeid, 'type_goods': type_goods,
        'new_goods': new_goods, 'page': page,
        'paginator': paginator, 'sortid': sortid,
        'type0': type0, 'type1': type1, 'type2': type2,
        'type3': type3, 'type4': type4, 'type5': type5,
    }
    return render(request, 'tt_goods/list.html', context)


def detail(request, id):
    # 获取所有分类
    type_list = TypeGoods.objects.all()
    type0 = type_list[0]
    type1 = type_list[1]
    type2 = type_list[2]
    type3 = type_list[3]
    type4 = type_list[4]
    type5 = type_list[5]
    # 获取对象id的商品
    goods = GoodsInfo.objects.get(pk=int(id))
    # 点击量+１
    goods.gclick += 1
    goods.save()
    type_goods = goods.gtype
    new_goods = type_goods.goodsinfo_set.order_by('-id')[0:2]
    context = {
        'title': '商品列表', 'goods': goods, 'new_goods': new_goods, 'type_goods': type_goods,
        'type0': type0, 'type1': type1, 'type2': type2,
        'type3': type3, 'type4': type4, 'type5': type5,
    }
    return render(request, 'tt_goods/detail.html', context)