from django.db import models
import uuid


class TechnicalTag(models.Model):
    # 纯随机数，与机器无关, 相重的几率很小。通常生成用户id用这个。
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, help_text=u'标签名称')
    svg_class = models.CharField(max_length=50, help_text=u'标签svgIcon的class')
    is_active = models.BooleanField(default=True, help_text=u'是否启用')
    sort_number = models.IntegerField(help_text=u'排序号码')
    is_delete = models.BooleanField(default=False, help_text=u'是否删除')
    # create_user = models.UUIDField(default=uuid.uuid4, null=False, help_text=u'创建用户', verbose_name=u'创建用户')
    create_user = models.IntegerField(null=False, help_text=u'创建用户')
    # auto_now_add=True 在model对象第一次被创建时,将字段的值设置为创建时的时间,
    # 以后修改对象时,字段的值不会再更新。
    create_time = models.DateTimeField(auto_now_add=True)
    # update_user = models.UUIDField(default=uuid.uuid4, null=False, help_text=u'更新用户', verbose_name=u'更新用户')
    update_user = models.IntegerField(null=False, help_text=u'创建用户')
    # auto_now=True 在保存该字段时,将其值设置为当前时间,并且每次修改model,都会自动更新
    update_time = models.DateTimeField(auto_now=True)

    # 在TechnicalTag.objects.get(name='vue')语句的结果中，显示字段name
    def __str__(self):
        return self.name

    # 内嵌类，给model定义元数据
    class Meta:
        # app名称
        app_label = 'xizhi_backend'
        verbose_name = u'技术标签'
        # admin管理系统中展现的名字
        verbose_name_plural = u'技术标签列表'
        # 指定表名
        db_table = 'technical_tag'
        # 排序字段,必须是tuple或list类型，带前缀-为倒序,比如[-'update_time']
        ordering = ['sort_number']
