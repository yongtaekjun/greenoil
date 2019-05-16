# companies/admin.py

from django.contrib import admin
from .models import (
    Company,
    City,
    OilCollectContract,
    OilCollector,
    Restaurant,
    OilCollectContract,
    UserRole,
)

admin.site.register(Company)
admin.site.register(City)
admin.site.register(OilCollectContract)
admin.site.register(OilCollector)
admin.site.register(Restaurant)
admin.site.register(UserRole)

admin.site.site_header = "Green Oil";
admin.site.site_title = "Green Oil";