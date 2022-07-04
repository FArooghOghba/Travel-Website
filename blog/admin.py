from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import *


# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = (
        'title',
        'author',
        'counted_views',
        'status',
        'publish_date',
        'created_date'
    )
    search_fields = ['title']
    list_filter = ['author', 'status']
    empty_value_display = '-empty-'
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'post',
        'email',
        'subject',
        'approved',
        'created_date'
    ]

    search_fields = ['email', 'subject']
    list_filter = ['email', 'approved']
    empty_value_display = '-empty-'


admin.site.register(Category)
