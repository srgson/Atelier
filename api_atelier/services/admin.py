from django.contrib import admin
from services.models import Claim, Telegram_manager


class ClaimAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'username',
        'phone_number',
        'message',
    )
    search_fields = ('username',)


class Telegram_managerAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'username',
        'email',
        'to_email',
        'telegram_id',
        'to_telegram'
    )
    search_fields = ('username',)


admin.site.register(Claim, ClaimAdmin)
admin.site.register(Telegram_manager, Telegram_managerAdmin)
