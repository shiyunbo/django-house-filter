from django.contrib import admin

# Register your models here.
from .models import House, Community


class CommunityAdmin(admin.ModelAdmin):

    '''设置列表可显示的字段'''
    list_display = ('name', 'city', )

    '''每页显示条目数'''
    list_per_page = 10

    '''设置可编辑字段'''
    list_editable = ('city',)

    '''按发布日期排序'''
    ordering = ('-mod_date',)


class HouseAdmin(admin.ModelAdmin):

    '''表单字段'''
    fields = ('description', 'community', 'bedroom', 'direction', 'floor', 'area', 'price', )

    '''设置列表可显示的字段'''
    list_display = ('description', 'community', 'price', 'bedroom', 'direction', 'floor', 'area', 'area_class', )

    '''设置过滤选项'''
    list_filter = ('bedroom', 'direction', 'floor', 'area_class')

    '''每页显示条目数'''
    list_per_page = 10

    '''设置可编辑字段'''
    list_editable = ('bedroom', 'direction', 'floor', 'area_class',)

    '''raw_id_fields'''
    raw_id_fields = ('community',)

    '''按发布日期排序'''
    ordering = ('-mod_date',)


admin.site.register(Community, CommunityAdmin)
admin.site.register(House, HouseAdmin)