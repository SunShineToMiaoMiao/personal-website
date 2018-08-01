from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
import uuid



# 视图函数 第一个参数是request
def index(request):
    # 将内容返回到网页上
    # return HttpResponse(u"Hello World 学而时习之")
    str_one = u'装修知识'
    tag_list = ["HTML", "CSS", "jQuery", "Python", "Django"]
    pig_obj = {
        'name': u'会跑的猪',
        'desc': u'耳朵跳来跳去的'
    }
    # 渲染模板
    # 默认配置下，Django 的模板系统会自动找到app下面的templates文件夹中的模板文件。
    return render(request, "learn_django/home.html",
                  {'name': str_one, 'tagList': tag_list,
                   'pigObj': pig_obj
                   })


def add_technical_tag(request):
    # tag_name = request.GET['tagName', '']
    tag_name = request.GET['tagName']
    bg_color = request.GET['bgColor']
    # u表示将后面跟的字符串以unicode格式存储
    str_show = tag_name + u'-----------' + bg_color
    return HttpResponse(str_show)


def add_technical_tag_2(request, tagName,  bgColor):
    print(u'354234234234234423432')
    print(request)
    # 基于MAC地址，时间戳，随机数来生成唯一的uuid，可以保证全球范围内的唯一性。
    tag_id = uuid.uuid1()
    # tag_name = request.GET['tagName']
    print(tagName)
    # bg_color = request.GET['bgColor']
    print(bgColor)
    # u表示将后面跟的字符串以unicode格式存储
    return HttpResponse(tagName + bgColor)


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add3(request, a, b):
    # 重定向 跳转至新地址
    return HttpResponseRedirect(
        reverse('add3', args=(a, b))
    )


def display_one(request):
    return render(request, "learn_django/demo_one.html")


