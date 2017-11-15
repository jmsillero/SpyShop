from rest_framework import viewsets
from test_app.models import Promotion
from test_app.serializer import PromotionSerializer

class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all();
    serializer_class = PromotionSerializer