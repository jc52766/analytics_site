from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='initiatives_home'),
    path('initiative_01/', views.init_01, name='init_01'),
    path('initiative_02/', views.init_02, name='init_02'),
]
