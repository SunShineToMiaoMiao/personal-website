from django.contrib import admin
from ..models import *


# Register your models here.
# TechnicalTag模型的管理器
@admin.register(TechnicalTag)
class TechnicalTag(admin.ModelAdmin):
    list_display=('name', 'svg_class', 'is_active', 'sort_number',
                  'create_time', 'update_time')
