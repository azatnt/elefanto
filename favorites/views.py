from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Favorite
from .serializers import *


class FavoriteList(generics.ListCreateAPIView):
    queryset = Favorite.objects.select_related('book', 'user').all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return FavoriteWriteSerializer
        return FavoriteReadSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
