from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>/', views.details, name='details'),
    path('members/detail_keluarga/<int:id>/', views.detail_keluarga, name='detail_keluarga'),
    path('keluarga/<int:id>/', views.detail_keluarga, name='detail_keluarga'),
    path('',views.dasboard, name='dashboard'),
]