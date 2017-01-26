from django.contrib import admin

from .models import Car, Manufacturer, Model


class CarAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Your Car', {
            'fields': ('name', 'vin', 'license_plate')
        }),
        ('Make & Model', {
            'fields': ('year', 'manufacturer', 'model')
        }),
        ('Tires', {
            'fields': ('tire_size', 'tire_pressure')
        }),
        ('Purchase/Sell Dates', {
            'fields': ('purchase_date', 'sell_date')
        })

    )

admin.site.register(Car, CarAdmin)
admin.site.register(Manufacturer)
admin.site.register(Model)
