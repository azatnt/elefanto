import django_filters
from .models import Book


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'genre__name': ['exact'],
            'author__name': ['exact'],
            'publication_date': ['exact', 'gte', 'lte'],
        }
