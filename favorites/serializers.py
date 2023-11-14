from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from book.serializers import BookSerializer
from .models import Favorite


class FavoriteWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['user', 'book']


class FavoriteReadSerializer(FavoriteWriteSerializer):
    book = BookSerializer()

    class Meta:
        model = Favorite
        fields = ['user', 'book']