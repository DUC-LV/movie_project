from django.contrib import admin

# Register your models here.
from .models import LiveTv


@admin.register(LiveTv)
class LiveTv(admin.ModelAdmin):
    list_display = [
        'created',
        '_id',
        'name',
        'description',
        'slug',
        'type',
        'coverImage',
        'horizontalImage',
        'needLogin',
        'price',
        'link'
    ]


admin.register(LiveTv)
