from django.db import models


class TechnicalTag(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    svg_class = models.CharField(max_length=50)
    is_enable = models.BooleanField()
    create_user = models.CharField(max_length=250)
    # 在model对象第一次被创建时,将字段的值设置为创建时的时间,
    # 以后修改对象时,字段的值不会再更新。
    create_time = models.DateTimeField(auto_now_add=True)
    update_user = models.CharField(max_length=250)
    # 在保存该字段时,将其值设置为当前时间,并且每次修改model,都会自动更新
    update_time = models.DateTimeField(auto_now=True)