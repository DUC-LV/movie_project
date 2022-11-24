from django.urls import path
from . import views

urlpatterns = [
    path('live-film/', views.live_film_list),
    path('live-film/<int:pk>/', views.live_film_detail),
]
