from django.contrib import admin
from .models import Contact


# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'subject',
        'email',
        'created_date'
    ]

    list_filter = ['email']
    search_fields = ['name', 'subject']