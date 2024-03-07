from rest_framework.viewsets import ModelViewSet

from categories.models import Category
from categories.api.serializers import CategorySerializer

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()