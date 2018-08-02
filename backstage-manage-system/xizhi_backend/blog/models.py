from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    qq = models.CharField(max_length=50)
    addr = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50)
    # 定义外键和一对一关系的时候需要加on_delete选项，此参数为了避免两个表里的数据不一致问题
    # CASCADE：级联删除; PROTECT：此值设置，是会报完整性错误。
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    on_delete = models.CASCADE
    content = models.TextField()
    score = models.TextField()
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name