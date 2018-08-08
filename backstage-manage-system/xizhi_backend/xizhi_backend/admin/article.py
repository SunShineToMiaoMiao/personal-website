from django.contrib import admin
from ..models import *


# article模型的后台管理设置
@admin.register(Article)
class Article(admin.ModelAdmin):
    list_display = ('title', 'author', 'content','create_time', 'update_time')
