from django.db import models
import uuid
from django.contrib.auth.models import User


class Article(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, help_text=u'文章标题')
    # 定义外键和一对一关系的时候需要加on_delete选项，此参数为了避免两个表里的数据不一致问题
    # CASCADE：级联删除; PROTECT：此值设置，是会报完整性错误。
    author = models.ForeignKey(User, on_delete=models.CASCADE, help_text=u'作者')
    excerpt = models.TextField(default=u'摘要', help_text=u'文章摘要')
    content = models.TextField(help_text=u'文章内容')
    is_delete = models.BooleanField(default=False, help_text=u'是否删除')
    create_user = models.IntegerField(null=False, help_text=u'创建用户')
    create_time = models.DateTimeField(auto_now_add=True)
    update_user = models.IntegerField(null=False, help_text=u'创建用户')
    update_time = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('TechnicalTag')

    def __str__(self):
        return self.title

    class Meta:
        # app名称
        app_label = 'xizhi_backend'
        # 指定表名
        db_table = 'article'
        verbose_name = u'文章'
        verbose_name_plural = u'文章列表'
