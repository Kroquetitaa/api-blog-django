from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from categories.models import Category
from categories.api.serializers import CategorySerializer
from categories.api.permissions import IsAdminOrReadOnly

class CategoryViewSet(ModelViewSet):
    
    permission_classes = [IsAdminOrReadOnly]
    
    serializer_class = CategorySerializer
    
    queryset = Category.objects.all()
    
    # queryset = Category.objects.filter(published=True)
    
    search_fields = ['id', 'published']
    
    lookup_field = 'id'
    
    filter_backends = [DjangoFilterBackend]
    
    filterset_fields = ['published']
    
    