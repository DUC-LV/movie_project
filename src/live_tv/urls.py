from django.urls import path
from . import views

urlpatterns = [
    path('live-tv/', views.live_tv_list),
    path('live-tv/<int:pk>/', views.live_tv_detail),
]
