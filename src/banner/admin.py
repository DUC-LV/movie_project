from django.contrib import admin

# Register your models here.
from .models import Banner


@admin.register(Banner)
class Banner(admin.ModelAdmin):
    list_display = [
        'created',
        '_id',
        'title',
        'message',
        'itemId',
        'itemType',
        'urlImage'
    ]


admin.register(Banner)
