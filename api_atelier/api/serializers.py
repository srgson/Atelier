from rest_framework import serializers
from services.models import Claim, Telegram_manager


class ClaimSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('username', 'phone_number', 'message')
        model = Claim


class Telegram_managerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'username',
            'email',
            'to_email',
            'telegram_id',
            'to_telegram'
        )
        model = Telegram_manager