from django.db import models
import uuid


class Author(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    qq = models.CharField(max_length=50)
    addr = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        # app名称
        app_label = 'xizhi_backend'
        # 指定表名
        db_table = 'author'
