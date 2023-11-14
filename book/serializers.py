from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
        ref_name = 'BookUser'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']


class BookSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True)
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'genre', 'author', 'publication_date', 'average_rating']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user = self.context['request'].user

        representation['average_rating'] = instance.calculate_average_rating()
        representation['is_favorite'] = instance.is_favorite(user)

        return representation


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['user', 'rating', 'text']

    def create(self, validated_data):
        book_id = self.context['view'].kwargs.get('pk')
        book = Book.objects.get(pk=book_id)
        user = self.context['request'].user
        review = Review.objects.create(book=book, user=user, **validated_data)
        return review


class BookDetailSerializer(BookSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta(BookSerializer.Meta):
        fields = BookSerializer.Meta.fields + ['description', 'reviews']
