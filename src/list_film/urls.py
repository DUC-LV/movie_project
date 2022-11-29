from django.urls import path
from . import views
urlpatterns = [
    path('list-film/', views.list_film_list),
    path('list-film/<str:slug>/', views.film_detail)
]
