from rest_framework.viewsets import ModelViewSet

from product.models import Product
from product.serializers.product_serializer import ProductSerializer
from rest_framework.permissions import IsAuthenticated  # authentication


class ProductViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]  # authentication
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by("id")  # ordenamento warning solved
