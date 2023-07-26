from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Claim(models.Model):
    username = models.CharField(
        max_length=255,
        verbose_name='Имя пользователя'
    )
    phone_number = models.CharField(
        max_length=12,
        verbose_name='Номер телефона'
    )
    message = models.TextField(
        verbose_name='Текст сообщения'
    )

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Telegram_manager(models.Model):
    username = models.CharField(
        max_length=255,
        verbose_name='Имя пользователя'
    )
    email = models.EmailField(blank=True)
    telegram_id = models.CharField(
        max_length=11,
        verbose_name='id Telegram'
    )
    to_telegram = models.BooleanField(
        default=True,
        verbose_name='Отправка в Telegram'
    )
    to_email = models.BooleanField(
        default=True,
        verbose_name='Отправка на почту'
    )

    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'
