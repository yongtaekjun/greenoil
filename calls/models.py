# calls/models.py

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

from companies.choices import (
    dict1,
    TUPLE2_CLIENT_REQUESTS ,
    TUPLE2_UINT_SYMBOLS,
    TUPLE1_PAID_METHODS,
    TUPLE1_PROCESSING_STATUS,
    TUPLE1_COMPANY_TYPES,
)

from companies.models import (
    Company, 
    Restaurant,
    OilCollector,
    OilCollectContract,
)

from enum import Enum

class PRODUCT (Enum):
    # from the restaurant
    USED_COOKING_OIL = 1
    # NEW_COOKING_OIL = 2
    # CHICKEN_BREAST = 3
    # CHICKEN_LEG = 4

    # NEW_COOKING_OIL = 1
    # CHICKEN_BREAST = 1
    # CHICKEN_BREAST = 1

    # from the oil collector
    OIL_TANK = 10
    REFINED_COOKING_OIL = 11

class Receipt(models.Model):

    # id              = models.AutoField( primary_key=True )
    seller          = models.ForeignKey( Restaurant, on_delete=models.CASCADE, related_name='receipt_seller')
    payer           = models.ForeignKey( OilCollector, on_delete=models.CASCADE, related_name='receipt_payer')

    paid_method     = models.PositiveSmallIntegerField(
        choices=TUPLE1_PAID_METHODS,
        default=5,
    )
    net_total       = models.DecimalField( max_digits = 10, decimal_places = 2,null=True, blank=True)
    tax_total       = models.DecimalField( max_digits = 10, decimal_places = 2,null=True, blank=True) # net amount
    # grand_total     = models.FloatField(default=0.0 ) # net amount

    scheduled_date  = models.DateTimeField(null=True, blank=True) # when will be paied, usally every end of month
    paid_date       = models.DateTimeField(null=True, blank=True) # when after paying
    image           = models.ImageField(default='default.jpg', upload_to='receipt_images',null=True, blank=True)

    def __str__(self):
        return '%s: for %s' % ( self.pk, self.seller )
    
    @property
    def description_of_paid_method (self):
        return dict (TUPLE1_PAID_METHODS) [self.paid_method]

class ReceiptStatement(models.Model):
    receipt         = models.ForeignKey( 'Receipt', on_delete=models.CASCADE, related_name='statements')
    description     = models.CharField(max_length = 64)
    unit_price      = models.DecimalField(max_digits=10, decimal_places=4)
    unit_symbol     = models.PositiveSmallIntegerField (
        choices=TUPLE2_UINT_SYMBOLS,
        default=1,
    )            
    how_many        = models.DecimalField(max_digits=10, decimal_places=2) # unit_price x how_many
    # tax_amount      = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '%s: on %s' % (self.receipt, self.description )

    @property
    def net_amount (self):
        "return location with json format"
        return self.unit_price * self.how_many

    @property
    def tax_amount (self):
        "return location with json format"
        return self.unit_price * self.how_many * 1.13

    @property
    def discription_of_unit_symbol (self):
        return dict1 (TUPLE2_UINT_SYMBOLS) [self.unit_symbol]


class ClientRequest(models.Model):
    category      = models.PositiveSmallIntegerField(
        choices=TUPLE2_CLIENT_REQUESTS,
        default=3, #Pickup
    )

    detail          = models.CharField  ( max_length=64, null=True, blank=True )
    client          = models.ForeignKey ( Company, on_delete = models.CASCADE, related_name = 'client_request_client')
    server          = models.ForeignKey ( Company, on_delete = models.CASCADE, related_name = 'client_request_server')
    requester       = models.ForeignKey ( User,    on_delete = models.CASCADE, related_name = 'client_request_requester')
    required_date   = models.DateTimeField() # when does the client want to pickup 

    def __str__(self):
        return '%s for %s on %s' % (self.description_of_category, self.client,  self.required_date )

    @property
    def description_of_category(self):
        return dict1 ( TUPLE2_CLIENT_REQUESTS ) [ self.category ]


class ProcessingStatus ( models.Model ):
    class Meta:
        verbose_name_plural = 'processing_status_set'

    original    = models.ForeignKey ( 
        ClientRequest, 
        on_delete=models.CASCADE,
        # related_name='processing_status_list'
    )
    status      = models.PositiveSmallIntegerField(
        choices=TUPLE1_PROCESSING_STATUS,
        default=1,
    )
    staff       = models.ForeignKey ( 
        User, 
        null = True, blank = True,
        on_delete = models.CASCADE, 
        related_name = "processing_status_by_me"
    ) # who will process , or who will be charged

    statement   = models.ForeignKey ( 
        ReceiptStatement, 
        null = True, blank = True,
        on_delete = models.CASCADE, 
        related_name = "processing_status_statement"
    ) # after completed when this is needed to be written on receipt as a statement

    created_on  = models.DateTimeField(default=timezone.now) 
    # scheduled_date  = models.DateTimeField(null=True) # when will be paied, usally every end of month

    def __str__(self):
        return '%s : %s' % (self.discription_of_status, self.original)

    @property
    def description_of_status(self):
        return dict (TUPLE1_PROCESSING_STATUS) [ self.status ]


class BillStatement(models.Model):
    receipt         = models.ForeignKey( 
        'Receipt', 
        blank=True, null=True, 
        on_delete=models.SET_NULL, 
        related_name='bill_statement_list'
    )
    description     = models.CharField(max_length = 64, blank=True, null=True)
    unit_price      = models.DecimalField(max_digits=10, decimal_places=4)
    unit_symbol     = models.PositiveSmallIntegerField (
        choices=TUPLE2_UINT_SYMBOLS,
        default=1,
    )            
    volume         = models.DecimalField(max_digits=10, decimal_places=2)
    created_on      = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s: on %s' % (self.receipt, self.description )

    @property
    def amount (self):
        "return unit_price * volume with json format"
        return self.unit_price * self.volume

    @property
    def tax (self):
        "return location with json format"
        return self.unit_price * self.volume * 0.13

    @property
    def total_amount (self):
        "return total amount with json format"
        return self.amount + self.tax

    @property
    def discription_of_unit_symbol (self):
        return dict1 (TUPLE2_UINT_SYMBOLS) [self.unit_symbol]

class PickupHistory ( models.Model ):
    class Meta:
        verbose_name_plural = 'history_list'

    restaurant      = models.ForeignKey(Restaurant, on_delete = models.SET_NULL ,blank=True, null=True)
    issue_date      = models.DateTimeField(default=timezone.now)

    schedule_date   = models.DateTimeField(blank=True, null=True)
    scheduler       = models.ForeignKey( # the person re-scheduleed
        User, 
        on_delete = models.SET_NULL ,
        blank=True, null=True, 
        related_name='scheduler_list'
    )

    complete_date   = models.DateTimeField(blank=True, null=True)
    trucker         = models.ForeignKey(
        User, 
        on_delete = models.SET_NULL,
        blank=True, null=True, 
        related_name='trucker_list'
    )
    
    bill_statement   = models.ForeignKey ( 
        BillStatement, 
        null = True, blank = True,
        on_delete = models.SET_NULL, 
        related_name = "task_descriptions"
    ) # after completed when this is needed to be written on receipt as a statement

    created_on  = models.DateTimeField(default=timezone.now) 
    scheduled_date  = models.DateTimeField(null=True, blank=True) # when will be paied, usally every end of month

    def __str__(self):
        return '%s : %s' % (self.discription_of_status, self.original)

    @property
    def description_of_status(self):
        return dict (TUPLE1_PROCESSING_STATUS) [ self.status ]




class PickupInterval(models.Model ):
    client          = models.ForeignKey( Company, on_delete=models.CASCADE,related_name = "pickup_interval_client")
    interval        = models.PositiveSmallIntegerField(default = 28 ) # 1 - 128 days ( ( last_pickup - completed_date ) + interval ) /2
    pickup_date     = models.DateTimeField()

    def __str__(self):
        return '%s: on %s' % (self.client, self.pickup_date )

# class TankRequest(models.Model):

#     category     = models.PositiveSmallIntegerField(
#         choices=CLIENT_REQUEST_CHOICES,
#         default=CLIENT_REQUEST.INSTALL,
#     )
#     client          = models.ForeignKey( Company, on_delete=models.CASCADE,related_name = "tank_request_client")
#     requester       = models.ForeignKey( User, on_delete = models.CASCADE, related_name = "tank_request_requester")
#     required_date   = models.DateTimeField() # when does the client want to pickup 
#     created_on      = models.DateTimeField( default=timezone.now) #when requested
#     litter          = models.PositiveSmallIntegerField() # when completed

#     def __str__(self):
#         return self.category


# class TankStatusChangeLog(models.Model):
#     FIRST_CALL  =  1
#     CONFIRMED   =  3
#     SCHEDULED   =  5
#     RESCHEDULED =  7
#     COMPLETED   =  9
#     DOCUMENTED  = 11
#     BILLED      = 13

#     PICKUP_STATUS_CHOICES = (
#         (FIRST_CALL, 'First Call'),
#         (CONFIRMED, 'Confirmed'),
#         (SCHEDULED, 'Scheduled'),
#         (RESCHEDULED, 'Re-scheduled'),
#         (COMPLETED, 'Completed'),
#         (DOCUMENTED, 'Documented'),
#         (BILLED, 'Billed'),
#     )

#     original    = models.ForeignKey( 'ClientRequest', on_delete=models.CASCADE, related_name = "tank_status_change_log_original")
#     status      = models.PositiveSmallIntegerField(
#         choices=PICKUP_STATUS_CHOICES,
#         default=FIRST_CALL,
#     )
#     handler   = models.ForeignKey( User, on_delete = models.CASCADE, related_name = "tank_status_change_log_handler") # when scheduled
#     created_on  = models.DateTimeField(default=timezone.now) # false when de-activate

#     def __str__(self):
#         return self.status
