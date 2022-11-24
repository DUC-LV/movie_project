from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import LiveStreaming


@admin.register(LiveStreaming)
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


admin.register(LiveStreaming)
