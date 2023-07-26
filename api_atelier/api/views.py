from rest_framework import mixins, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import (ClaimSerializer, ServicePriceSerializer,
                             Telegram_managerSerializer)
from info.models import ServicePrice
from services.models import Claim, Telegram_manager


@api_view(['POST'])
def create_claim(request):
    serializer = ClaimSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    Claim.objects.create(**serializer.validated_data)
    manager = Telegram_manager.objects.all()[0]
    return Response(
        data={
            'username': manager.username,
            'email': manager.email,
            'to_email': manager.to_email,
            'telegram_id': manager.telegram_id,
            'to_telegram': manager.to_telegram
        },
        status=status.HTTP_201_CREATED
    )


class ManagersListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = Telegram_managerSerializer
    queryset = Telegram_manager.objects.all()


class ServicePriceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ServicePrice.objects.all()
    serializer_class = ServicePriceSerializer
