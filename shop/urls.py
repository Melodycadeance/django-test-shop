from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.items_list, name='items_list'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
]