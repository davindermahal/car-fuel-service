from django.contrib import admin

from .models import Brand, FillUp, Location, Payment

admin.site.register(Brand)
admin.site.register(FillUp)
admin.site.register(Location)
admin.site.register(Payment)