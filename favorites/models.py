from django.contrib.auth.models import User
from django.db import models

from book.models import BaseModel, Book


class Favorite(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='favorites')

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
