from django.urls import path
from .views import *

urlpatterns = [
    path('', BookList.as_view(), name='book-list'),
    path('<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
]
