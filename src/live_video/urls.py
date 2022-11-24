from django.urls import path
from . import views

urlpatterns = [
    path('live-video/', views.live_video_list),
    path('live-video/<int:pk>/', views.live_video_detail),
]
