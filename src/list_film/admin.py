from django.contrib import admin
from .models import TopicFilm, ListFilm
from guardian.admin import GuardedModelAdmin


# Register your models here.

@admin.register(TopicFilm)
class TopicFilm(GuardedModelAdmin):
    list_display = [
        'created',
        '_id',
        'name',
        'description',
        'slug',
        'type',
        'itemType',
    ]


admin.register(TopicFilm)


@admin.register(ListFilm)
class ListFilm(GuardedModelAdmin):
    list_display = [
        'created',
        '_id',
        'name',
        'coverImage',
        'coverImageH',
        'type',
        'description',
        'slug',
        'link',
        'model_chaID'
    ]


admin.register(ListFilm)
