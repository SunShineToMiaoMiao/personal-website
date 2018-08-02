from django.db import models


class Author(models.Model):
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
