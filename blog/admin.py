from django.contrib import admin
from .models import Post


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'counted_views',
        'status',
        'publish_date',
        'created_date'
    )
    search_fields = ['title']
    list_filter = ['status']
    empty_value_display = '-empty-'
