from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import LiveVideo
from guardian.admin import GuardedModelAdmin


@admin.register(LiveVideo)
class Banner(GuardedModelAdmin):
    list_display = [
        'created',
        '_id',
        'name',
        'description',
        'slug',
        'durationStr',
        'coverImage',
        'link',
    ]


admin.register(LiveVideo)
