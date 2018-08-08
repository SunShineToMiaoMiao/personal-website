import json
from django.http import HttpResponse
from django.core import serializers
from xizhi_backend.models import *


def get_list(request):
    """
    获取文章列表--ORM函数学习
    :param request:
    :return:

    all()返回的是QuerySet 数据类型；values()返回的是ValuesQuerySet 数据类型
    select_related 优化一对一，多对一查询 获取相应外键对应的对象
    defer 排除不需要的字段
    only 仅选择需要的字段；若此字段不是class中默认显示的字段，则会根据id循环查询；
    prefetch_related 优化一对多，多对多查询

    """

    # article_list = Article.objects.values('title')

    # all()返回的是QuerySet 数据类型；values()返回的是ValuesQuerySet 数据类型
    # article_list = Article.objects.all()[:10]

    # select_related 优化一对一，多对一查询 获取相应外键对应的对象
    # defer 排除不需要的字段
    # only 仅选择需要的字段；若此字段不是class中默认显示的字段，则会根据id循环查询；
    # prefetch_related 优化一对多，多对多查询
    print('文章列表\n')
    article_list = Article.objects.all() \
            .defer('content')[:10]
    rs = list(article_list)
    print(rs)

    print('文章列表3\n')
    article_list_3 = Article.objects.all() \
        .only('title')[:10]
    print(list(article_list_3))
    # rs_json = serializers.serialize('json', article_list)
    # print(rs_json)

    # a1 = article_list[0]
    # print(a1)
    # print(a1.author.name)
    # print(a1.tags.all())

    # prefetch_related 优化一对多，多对多查询
    # article_list_2 = Article.objects.all().prefetch_related('tags')[:3]
    article_list_2 = Article.objects.filter(id=12).prefetch_related('tags')[:3]

    # for a in article_list_2:
    #     print(a.title)
    #     print(a.tags.all())

    # return HttpResponse(json.dumps(rs), content_type="application/json")
    # return HttpResponse(json.dumps(a1), content_type="application/json")
    # return HttpResponse(a1, content_type="application/json")
    # return HttpResponse(rs_json, content_type="application/json")
    return HttpResponse('asfsdfsadf', content_type="application/json")


def get_count(request):
    pass
    # Article.objects.all().values('author_id')\
    #     .annotate(count=Count('author'))\
    #     .values('author_id', 'count').query.__str__()

    # Article.objects.all().values('author_id').annotate(count=Count('author')).values('author_id', 'count')