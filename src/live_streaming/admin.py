from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import LiveStreaming
from guardian.admin import GuardedModelAdmin


@admin.register(LiveStreaming)
class Banner(GuardedModelAdmin):
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
