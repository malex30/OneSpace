from django.urls import path
from . import views



urlpatterns = [
    path('', views.log_and_reg),
    path('home', views.home),
    path('new_releases', views.new_releases),
]
