from django.contrib import admin

# Register your models here.
from .models import LiveTv
from guardian.admin import GuardedModelAdmin


@admin.register(LiveTv)
class LiveTv(GuardedModelAdmin):
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
