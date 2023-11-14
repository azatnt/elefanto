from django.urls import path
from .views import *

urlpatterns = [
    path('', FavoriteList.as_view(), name='favorite-list'),
]
