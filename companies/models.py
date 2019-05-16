#companies/models.py

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from djchoices import ChoiceItem, DjangoChoices

# from users.models import UserRole
from enum import Enum
from django.urls import reverse
from .choices import TUPLE2_USER_ROLES, dict1, TUPLE1_DIVISIONS,TUPLE1_TANK_SIZES

class City(models.Model):
    city        = models.CharField(max_length=64)
    province    = models.CharField(max_length=64, default = 'Ontario')
    country     = models.CharField(max_length=64, default = 'Canada')

    def __str__(self):
        return '%s, %s' % ( self.city, self.province )

class Company(models.Model):
    short_name      = models.CharField(max_length= 32, primary_key=True, unique=True)
    full_name       = models.CharField(max_length=128)
    unit_number     = models.CharField(max_length=4, null=True, blank=True )
    street          = models.CharField(max_length=128)
    city            = models.ForeignKey(
        'City',
        related_name = 'company_city',
        on_delete=models.CASCADE
    )
    postal_code     = models.CharField(max_length=128)
    phone           = models.CharField(max_length=16)
    latitude        = models.FloatField (null=True, blank=True)
    longitude       = models.FloatField (null=True, blank=True)
    staffs          = models.ManyToManyField(
        User,
        through='UserRole',
        through_fields=('company','user' )
        # blank = True,
    )
    image = models.ImageField(default='company_images/default.jpg', upload_to='company_images', null=True, blank=True)

    registered_on   = models.DateTimeField ( default=timezone.now)
    approved_on     = models.DateTimeField ( null=True, blank = True ) # when this is created by guest user
    is_active       = models.BooleanField ( default=False, null=True, blank = True) # false when de-activate

    def __str__(self):
        return self.short_name

    @property
    def address (self):
        "return full address"
        if self.unit_number :
            return 'unit# %s, %s %s %s' % ( self.unit_number, self.street, self.city, self.postal_code )

        return '%s, %s %s' % ( self.street, self.city, self.postal_code )

    @property
    def location (self):
        "return location with json format"
        if self.latitude is None or self.longitude is None: return

        return '{ latitude: %f, longitude: %f }' % ( self.latitude, self.longitude )

    #--- method overriding
    def save(self, *args, **kwargs):
        # do_something()
        super().save(*args, **kwargs)  # Call the "real" save() method.
        # do log there is a new branch registerated

class UserRole ( models.Model ):

    user        = models.ForeignKey ( User, on_delete=models.CASCADE, related_name='userrole')
    company     = models.ForeignKey ( 'Company', on_delete=models.CASCADE, )
    role        = models.PositiveSmallIntegerField(
        choices=TUPLE2_USER_ROLES,
        default=111,
    )

    is_active   = models.BooleanField (default=False) # false when de-activate
    started_on  = models.DateTimeField (null=True, blank = True ) # when this role started

    class Meta:
        # auto_created = True
        unique_together = ( ('user', 'company', 'role'), )

    def __str__(self):
        return '%s : %s at %s' % (self.user.username, self.description_of_role, self.company )

    @property
    def description_of_role(self):
        return dict1 (TUPLE2_USER_ROLES) [self.role]
# Chowon, Cho Won Family Restaurant, 43.786781, -79.418169 17 Drewry Ave, North York, ON M2M 1C9
# Owl of Minerva, The Famous Owl of Minerva, 43.773358,, -79.414198, 5324 Yonge St, North York, ON M2N 5P9
# 1027 Finch Ave W
# North York, ON M3J 2C7
# 43.767766, -79.469641
class Restaurant(Company):

    # https://docs.djangoproject.com/en/2.1/topics/db/models/#multi-table-inheritance
    company = models.OneToOneField (
        Company, 
        on_delete=models.CASCADE,
        related_name = 'restaurant_company',
        parent_link=True,
    )
    division = models.SmallIntegerField(
        choices=TUPLE1_DIVISIONS,
        default=225,
    )

    def __str__(self):
        return f'{self.short_name}' 

    # def get_absolute_url(self):
    #     return reverse( 'restaurant_detail', kwargs={'pk': self.pk} )

    def get_absolute_url(self):
        return reverse( 'restaurant_list' )


# Greenoil-Toronto, Green Oil Incorperation, 43.764513, -79.477646 4490 Chesswood Dr North York, ON M3J 2B9, 416-633-8846
# Greenoil-Barrie, Green Oil Barrie, 44.380485 , -79.702912 , 39 Anne St S, Barrie, ON L4N 2C7
class OilCollector(Company):

    # https://docs.djangoproject.com/en/2.1/topics/db/models/#multi-table-inheritance
    company = models.OneToOneField (
        Company, 
        on_delete=models.CASCADE,
        # related_name = 'oil_collector_company',
        parent_link=True,
    )

    def __str__(self):
        return f'{self.short_name} ' 


class OilCollectContract(models.Model):

    restaurant      = models.OneToOneField ( 
        'Restaurant',
        primary_key = True,
        on_delete=models.CASCADE, 
        related_name='contract'
    )

    collector      = models.ForeignKey ( 
        'OilCollector', 
        on_delete=models.CASCADE, 
        related_name='contract_list'
    )

    rate        = models.DecimalField(max_digits=10, decimal_places=4) #price per litter

    tank_size   = models.PositiveSmallIntegerField(
        choices = TUPLE1_TANK_SIZES,
        default = 200,
    )
    tank_direction  = models.PositiveSmallIntegerField( default =  7) # from front door
    tank_distance   = models.PositiveSmallIntegerField( default = 10) # meter

    is_active       = models.BooleanField(default=True) #if contract changed it should be deactivated
    referal         = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        # related_name='referal',
        null = True, blank = True,
    )
    agreeded_on     = models.DateTimeField()

    def __str__(self):
        return '%s-$ %.4f - Tank:%d L -%d H-%d MT by %s on %s' % (
            self.restaurant, 
            self.rate, 
            self.tank_size, 
            self.tank_direction,
            self.tank_distance,
            self.referal,
            self.agreeded_on,
        )

    def description_of_tank_size(self):
        return dict (TUPLE1_TANK_SIZES) [self.tank_size]

