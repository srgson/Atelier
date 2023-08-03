from django.contrib import admin

from .models import ServicePrice, Bot, Images


class ServicePriceAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'title', 'ot', 'price', 'sort_position',
    )


class BotAdmin(admin.ModelAdmin):
    list_display = ('username', 'token', 'active')


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')


admin.site.register(ServicePrice, ServicePriceAdmin)
admin.site.register(Bot, BotAdmin)
admin.site.register(Images, ImagesAdmin)
