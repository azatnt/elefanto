from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import *
from .filters import BookFilter
from .serializers import *


class BookList(generics.ListAPIView):
    queryset = Book.objects.select_related('genre', 'author').prefetch_related('favorites').all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter


class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.select_related('genre', 'author').prefetch_related('favorites', 'reviews').all()
    serializer_class = BookDetailSerializer
    permission_classes = (IsAuthenticated, )


class ReviewList(generics.CreateAPIView):
    queryset = Review.objects.select_related('book', 'user').all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        book_id = self.kwargs.get('pk')
        return Review.objects.filter(book_id=book_id)
