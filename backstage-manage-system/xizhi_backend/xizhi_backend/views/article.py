import json
from django.http import HttpResponse
from xizhi_backend.models import *


def get_list(request):
    # tag_list = TechnicalTag.objects.all().value('name', 'sort_number')
    tag_list = TechnicalTag.objects.values('name', 'sort_number')
    print(tag_list)
    print('执行SQL')
    print(str(TechnicalTag.objects.all().query))
    rs = list(tag_list)
    return HttpResponse(json.dumps(rs), content_type="application/json")