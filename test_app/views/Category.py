from rest_framework import viewsets
from test_app.serializer import CategorySerializer
from test_app.models import Category

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


