from django.urls import path
from . import views
urlpatterns = [
    path('list-film/', views.list_film_list),
]
