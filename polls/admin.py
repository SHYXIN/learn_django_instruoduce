from django.contrib import admin
from .models import Choice, Question


# Register your models here.
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']
#
#
# admin.site.register(Question, QuestionAdmin)
#
#

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]


# class ChoiceInline(admin.StackedInline):
#     """堆叠式，宽松"""
#     model = Choice
#     extra = 3

class ChoiceInline(admin.TabularInline):
    """内联式，紧凑"""
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]  # 内部行
    # 列表页显示详情
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 增加过滤器
    list_filter = ['pub_date']
    # 增加一个搜索框
    search_fields = ['question_text']
    # 分页器
    list_per_page = 2



admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
