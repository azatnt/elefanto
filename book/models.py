from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Genre(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Author(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(BaseModel):
    title = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='books')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_date = models.DateField()
    description = models.TextField()
    average_rating = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.title

    def is_favorite(self, user):
        return self.favorites.filter(user=user).exists()

    def calculate_average_rating(self):
        reviews = self.reviews.all()

        if reviews.exists():
            total_rating = sum(review.rating for review in reviews)
            return total_rating / reviews.count()
        else:
            return 0 if not self.average_rating else self.average_rating


class Review(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    text = models.TextField()

    def __str__(self):
        return f"{self.book.title} - {self.user.username}"
