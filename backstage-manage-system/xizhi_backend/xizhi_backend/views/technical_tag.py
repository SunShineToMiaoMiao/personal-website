import json
from django.http import HttpResponse
from xizhi_backend.models import *


def get_list(request):
    # tag_list = TechnicalTag.objects.all().extra(select={'tag_name': 'name'}).defer('name')
    # tag_list = TechnicalTag.objects.all().extra(select={'tag_name': 'name'})
    # 只需要一个字段
    tag_list = TechnicalTag.objects.values_list('name',flat=True)
    print(tag_list)
    print('执行SQL')
    # print(str(TechnicalTag.objects.all().extra(select={'tag_name': 'name'}).defer('name').query))
    print(str(TechnicalTag.objects.values_list('name',flat=True).query))
    rs = list(tag_list)
    print(json.dumps(rs))
    print(rs)
    # return HttpResponse(rs, content_type="application/json")
    return HttpResponse(json.dumps(rs), content_type="application/json")