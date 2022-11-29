from django.urls import path, re_path
from . import views

urlpatterns = [
    path('live-film/', views.live_film_list),
    path('live-film/<str:slug>/', views.live_film_detail),
    path('search/', views.test_search),
]
