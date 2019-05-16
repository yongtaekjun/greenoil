# calls/admin.py

from django.contrib import admin
from import_export import resources
from django.contrib.auth.models import User

from .models  import ( 
    ClientRequest, 
    Receipt,
    ReceiptStatement,
    BillStatement,
    PickupHistory,
    ProcessingStatus,
    PickupInterval,
)

from companies.models  import ( 
    Restaurant, 
    OilCollector,
)

# Register your models here.
admin.site.register( ClientRequest )
admin.site.register( Receipt )
admin.site.register( ReceiptStatement )
admin.site.register( ProcessingStatus )
admin.site.register( PickupInterval )
admin.site.register( PickupHistory )
admin.site.register( BillStatement )

class UserResource ( resources.ModelResource):
    class Meta:
        model = User


class RestaurantResource ( resources.ModelResource):
    class Meta:
        model = Restaurant

class eOilCollectorResourc ( resources.ModelResource):
    class Meta:
        model = OilCollector


