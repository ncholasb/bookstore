from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.serializers import OrderSerializer
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
)  # Auth
from rest_framework.permissions import IsAuthenticated  # needs auth


class OrderViewSet(ModelViewSet):
    authentication_classes = [
        SessionAuthentication,
        BasicAuthentication,
        TokenAuthentication,
    ]  # auth viewset
    permission_classes = [IsAuthenticated]

    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by("id")  # ordenamento warning solved
