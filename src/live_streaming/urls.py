from django.urls import path
from . import views

urlpatterns = [
    path('live-streaming/', views.live_streaming_list),
    path('live-streaming/<int:pk>/', views.live_streaming_detail),
]
