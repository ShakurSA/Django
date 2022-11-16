from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('main/', main, name='main'),
]

