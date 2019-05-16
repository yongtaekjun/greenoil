# calls/make_sample_data.py

import pytz
import django.utils.timezone as tz
from datetime import datetime as dt

from calls.models import ( 
    Receipt, 
    BillStatement, 
    # ReceiptStatement, 
    # ClientRequest, 
    # ProcessingStatus,
    PickupHistory,
)

from companies.models import (
    City,
    Restaurant,
    OilCollector, 
    OilCollectContract,
    UserRole,
)

from users.models import ( 
    UserProfile, 
)
from companies.choices import TUPLE2_USER_ROLES, dict1, TUPLE1_DIVISIONS,TUPLE1_TANK_SIZES

from django.contrib.auth.models import User

'''
This make test data in database
'''
def make_all_sample_data ():

    make_sample_user()
    make_sample_city()
    make_sample_oil_collector()
    make_sample_restaurant()
    make_sample_user_role()
    make_sample_contract()

def make_sample_city():

    City.objects.all (). delete ()

    City.objects.create (
        city = 'North York',
        province = 'Ontario',
        country = 'Canada',
    ).save()

    City.objects.create (
        city = 'Toronto',
        province = 'Ontario',
        country = 'Canada',
    ).save()
    
    City.objects.create (
        city = 'Barrie',
        province = 'Ontario',
        country = 'Canada',
    ).save()
    
    City.objects.create (
        city = 'New Market',
        province = 'Ontario',
        country = 'Canada',
    ).save()
    
    City.objects.create (
        city = 'Richmod Hills',
        province = 'Ontario',
        country = 'Canada',
    ).save()
    
    City.objects.create (
        city = 'Dallas',
        province = 'Texas',
        country = 'USA',
    ).save()

def make_sample_oil_collector():
    
    OilCollector.objects.all().delete()

    OilCollector.objects.create (
        short_name = 'Greenoil Toronto',
        full_name = 'Green Oil Inc',

        unit_number = '9A',
        street = '4490 Chesswood Dr',
        city = City.objects.get (city = 'Toronto'),
        postal_code = 'M2N4R9',
        phone = '4168881234',
        latitude = 43.764513,
        longitude = -79.477646,
    ).save()

    OilCollector.objects.create (
        short_name = 'Greenoil Barrie',
        full_name = 'Green Oil Barrie Inc',

        # unit_number = '9A'
        street = '39 Anne St S.',
        city = City.objects.get (city = 'Barrie'),
        postal_code = 'N2N4R9',
        phone = '9058881235',
        latitude = 44.380485,
        longitude = -79.702912,
    ).save()

def make_sample_restaurant():

    Restaurant.objects.all (). delete ()

    Restaurant.objects.create (
        short_name = 'Chowon',
        full_name = 'Chown Familly Restaurant',
        unit_number = '5',
        street = '17 Drewry Ave',
        city = City.objects.get (city = 'North York'),
        postal_code = 'M2M 1C9',
        phone = '4168851234',
        latitude = 43.786781,
        longitude = -79.418169,

    ).save()

    Restaurant.objects.create (
        short_name = 'Owl of Minerva',
        full_name = 'The Famous Owl of Minerva',
        street = '5324 Yonge St',
        city = City.objects.get (city = 'North York'),
        postal_code = 'M2N 5P9',
        phone = '4168831234',
        latitude = 43.773358,
        longitude = -79.414198,

    ).save()
 
    Restaurant.objects.create (
        short_name = 'Daio',
        full_name = 'Daio Japanese Restaurant',
        street = '45 Carlton St',
        city = City.objects.get (city = 'Toronto'),
        postal_code = 'M5B 2H9',
        phone = '6478831234',
        latitude = 43.661420,
        longitude = -79.380906,

    ).save()


def make_sample_user_role():
    
    UserRole.objects.all (). delete ()

    # CEO -------------------------------------------------------------------
    UserRole.objects.create (
        user = User.objects.get ( username = 'hyunjung'),
        company = OilCollector.objects.get ( short_name = 'Greenoil Toronto'),
        role = TUPLE2_USER_ROLES[0][1][0][0],
    ).save()
    # trucker ---------------------------------------------------------------
    UserRole.objects.create (
        user = User.objects.get ( username = 'hyunjung'),
        company = OilCollector.objects.get ( short_name = 'Greenoil Toronto'),
        role = TUPLE2_USER_ROLES[1][1][1][0],
    ).save()

    UserRole.objects.create (
        user = User.objects.get ( username = 'changho'),
        company = OilCollector.objects.get ( short_name = 'Greenoil Toronto'),
        role = TUPLE2_USER_ROLES[1][1][1][0],
    ).save()

    # Tank Installer --------------------------------------------------------
    UserRole.objects.create (
        user = User.objects.get ( username = 'haeseung'),
        company = OilCollector.objects.get ( short_name = 'Greenoil Toronto'),
        role = TUPLE2_USER_ROLES[1][1][2][0],
    ).save()

    # Dispatcher -------------------------------------------------------------
    UserRole.objects.create (
        user = User.objects.get ( username = 'moonyoung'),
        company = OilCollector.objects.get ( short_name = 'Greenoil Toronto' ),
        role = TUPLE2_USER_ROLES[1][1][4][0],
    ).save()

    # Marketer/Sales----------------------------------------------------------
    UserRole.objects.create (
        user = User.objects.get ( username = 'moonyoung'),
        company = OilCollector.objects.get ( short_name = 'Greenoil Toronto'),
        role = TUPLE2_USER_ROLES[1][1][2][0],
    ).save()

    # Restaurant Owner ------------------------------------------------------
    UserRole.objects.create (
        user = User.objects.get ( username = 'jongsik'),
        company = Restaurant.objects.get ( short_name = 'Chowon'),
        role = TUPLE2_USER_ROLES[0][1][0][0],
    ).save()

    UserRole.objects.create (
        user = User.objects.get ( username = 'soonseok'),
        company = Restaurant.objects.get ( short_name = 'Owl of Minerva'),
        role = TUPLE2_USER_ROLES[0][1][0][0],
    ).save()

    UserRole.objects.create (
        user = User.objects.get ( username = 'soonjoo'),
        company = Restaurant.objects.get ( short_name = 'Daio'),
        role = TUPLE2_USER_ROLES[0][1][0][0],
    ).save()

def make_sample_user():

    User.objects.exclude (username = 'admin').delete()

    User.objects.create (
        username = 'soonseok',
        password = 'greenoil001',
        email = 'soonseok@gmail.com',
        first_name = 'Soonseok',
        last_name = 'Cha',
    ).save()

    User.objects.create (
        username = 'hyunjung',
        password = 'greenoil001',
        # password2 = 'greenoil001',
        email = 'hyunjung@gmail.com',
        first_name = 'hyunjung',
        last_name = 'Kim',
    ).save()

    User.objects.create (
        username = 'haesoo',
        password = 'greenoil001',
        # password2 = 'greenoil001',
        email = 'haesoo@gmail.com',
        first_name = 'Haesoo',
        last_name = 'Kim',
    ).save()


    User.objects.create (
        username = 'yongtaek',
        password = 'greenoil001',
        # password2 = 'greenoil001',
        email = 'yongtaek@gmail.com',
        first_name = 'yongtaek',
        last_name = 'jun',
    ).save()

    User.objects.create (
        username = 'jongsik',
        password = 'greenoil001',
        # password2 = 'greenoil001',
        email = 'jongsik@gmail.com',
        first_name = 'Jongsik',
        last_name = 'Kim',
    ).save()

    User.objects.create (
        username = 'donghan',
        password = 'greenoil001',
        # password2 = 'greenoil001',
        email = 'donghan@gmail.com',
        first_name = 'Donghan',
        last_name = 'Cho',
    ).save()

    User.objects.create (
        username = 'moonyoung',
        password = 'greenoil001',
        # password2 = 'greenoil001',
        email = 'moonyoung@gmail.com',
        first_name = 'Moonyoung',
        last_name = 'Lee',
    ).save()

    User.objects.create (
        username = 'changho',
        password = 'greenoil001',
        # password2 = 'greenoil001',
        email = 'changho@gmail.com',
        first_name = 'Changho',
        last_name = 'Moon',
    ).save()


    User.objects.create (
        username = 'haeseung',
        password = 'greenoil001',
        # password2 = 'greenoil001',
        email = 'haeseung@gmail.com',
        first_name = 'Haeseung',
        last_name = 'Lee',
    ).save()


def make_sample_contract():
    
    OilCollectContract.objects.all().delete ()

    OilCollectContract.objects.create (
        restaurant  = Restaurant.objects.get ( short_name = 'Chowon'),
        collector   = OilCollector.objects.get ( short_name = 'Greenoil Toronto'),
        rate        = 0.023,
        tank_size   = TUPLE1_TANK_SIZES[1][0], #200 L
        tank_direction = 7,
        tank_distance = 10,
        referal     = User.objects.get ( username = 'haesoo'),
        agreeded_on = tz.make_aware ( 
            dt.strptime('2019-04-20', "%Y-%m-%d"),
            pytz.timezone('America/Toronto'),
        )
    ).save()

    OilCollectContract.objects.create (
        restaurant  = Restaurant.objects.get ( short_name = 'Owl of Minerva'),
        collector   = OilCollector.objects.get ( short_name = 'Greenoil Toronto'),
        rate        = 0.024,
        tank_size   = TUPLE1_TANK_SIZES[2][0], #400 L
        tank_direction = 7,
        tank_distance = 10,
        referal     = User.objects.get ( username = 'haesoo'),
        agreeded_on = tz.make_aware ( 
            dt.strptime('2019-04-15', "%Y-%m-%d"),
            pytz.timezone('America/Toronto'),
        )
    ).save()

    OilCollectContract.objects.create (
        restaurant  = Restaurant.objects.get ( short_name = 'Daio'),
        collector   = OilCollector.objects.get ( short_name = 'Greenoil Toronto'),
        rate        = 0.019,
        tank_size   = TUPLE1_TANK_SIZES[2][0], #400 L
        tank_direction = 7,
        tank_distance = 10,
        referal     = User.objects.get ( username = 'haesoo'),
        agreeded_on = tz.make_aware ( 
            dt.strptime('2019-04-15', "%Y-%m-%d"),
            pytz.timezone('America/Toronto'),
        )
    ).save()

    # to confirm
    ct_list = OilCollectContract.objects.all()
    