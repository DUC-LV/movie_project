from django.urls import path
from . import views

urlpatterns = [
    path('banner/', views.banner_list),
    path('banner/<int:pk>/', views.banner_detail),
]
