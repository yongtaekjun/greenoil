# calls/schedule.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import ( 
    Receipt, ReceiptStatement, ClientRequest, ProcessingStatus,
    PickupHistory,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from calls.views import get_next_pickup_date, get_pickup_interval

'''
This auto scheduling will be run every day
'''
def make_pickup_schedule():
    restaurant_list = Restaurant.objects.all()
    for restaurant in restaurant_list:
        try:
            last_schedule = PickupHistory.objects.filter(restaurant=restaurant).order_by('-schedule_date')[0]
            #already scheduled but not completed. we don't need to re-schedule
            if last_schedule.complete_date is None:
                continue

            last_pickup_date = last_schedule.complete_date
        # if this is first time use this system 
        except PickupHistory.DoesNotExist():
            last_pickup_date = datetime.datetime.now()

        next_pickup_date = last_pickup_date + timedelta ( days = get_pickup_interval(restaurant))

        PickupHistory.objects.create (
            restaurant = restaurant,
            schedule_date = next_pickup_date,
        ).save()

'''
prepare_next_receipt() will run every month for auto scheduling
'''

def prepare_next_receipt():

    pass
