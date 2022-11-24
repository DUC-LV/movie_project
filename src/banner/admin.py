from django.contrib import admin

# Register your models here.
from .models import Banner
from guardian.admin import GuardedModelAdmin


@admin.register(Banner)
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


admin.register(Banner)
