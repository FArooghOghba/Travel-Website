from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
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


admin.site.register(Category)
