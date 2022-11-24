from django.contrib import admin
from .models import LiveFilm
from guardian.admin import GuardedModelAdmin


@admin.register(LiveFilm)
class Banner(GuardedModelAdmin):
    list_display = [
        'created',
        '_id',
        'name',
        'coverImage',
        'coverImageH',
        'description',
        'slug',
        'type',
        'link',
    ]


admin.register(LiveFilm)
