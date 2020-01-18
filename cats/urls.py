"""Cats app URL config"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='gatitos'),
    path('crear', views.create, name='create_cat'),
]