from django.contrib import admin

from .models import ServicePrice


class ServicePriceAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'title', 'ot', 'price', 'sort_position',
    )


admin.site.register(ServicePrice, ServicePriceAdmin)
