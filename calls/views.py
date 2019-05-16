# calls/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Receipt, ReceiptStatement, ClientRequest, ProcessingStatus, PickupInterval,PickupHistory
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from datetime import timedelta, datetime, date, time

def get_pickup_interval (restaurant):
    try:
        pickup_date_list = PickupHistory.objects.filter(restaurant=restaurant).order_by('-complete_date')[:5].complete_date
    except PickupHistory.DoesNotExist():
        return random.randrange( 8, 22, 1)

    pickup_count = 0
    interval_total = 0
    for pickup_date in pickup_date_list:
        pickup_count += 1
        if pickup_count == 1: # can not compare with only one item
            prev_date = pickup_date
            continue
        interval_total += (pickup_date - prev_date )
        prev_date = pickup_date

    if pickup_count == 1: # if first used
        return random.randrange( 8, 22, 1)

    return int( interval_total / pickup_count -1 )


def get_next_pickup_date (restaurant):
    try:
        last_schedule = PickupHistory.objects.filter(restaurant=restaurant).order_by('-schedule_date')[0]
        if last_schedule.complete_date is None: #already scheduled but not completed
            return last_schedule.scheduled_date

        last_pickup_date = last_schedule.complete_date

    except PickupHistory.DoesNotExist():
        last_pickup_date = datetime.datetime.now()

    return last_pickup_date + timedelta ( days = get_pickup_interval(restaurant))

class ClientRequestListView ( LoginRequiredMixin, UserPassesTestMixin, ListView ):
    model = ClientRequest
    template_name = 'calls/list.html'
    context_object_name = 'calls'
    ordering = ['-required_date']
    # queryset = ClientRequest.prefetch_related('processing_status_list').all()
    def test_func(self):
        # roles = self.get_object()
        # if self.request.user == 'admin':
        #     return True
        return True

    # def get_queryset(self):
    #     processing_status = get_object_or_404(ProcessingStatus, original = self.kwargs.get('processingstatus'))
    #     return Post.objects.filter(author=user).order_by('-date_posted')

class CallHistoryListView ( LoginRequiredMixin, UserPassesTestMixin, ListView ):
    model = ProcessingStatus
    template_name = 'calls/history_list.html'
    context_object_name = 'histories'
    ordering = ['created_on']
    def test_func(self):
        # roles = self.get_object()
        # if self.request.user == 'admin':
        #     return True
        return True
    # def get_queryset(self):
    #     first_call = get_object_or_404(ClientRequest, pk = self.kwargs.get('original'))
    #     return ProcessingStatus.objects.filter(original=first_call).order_by('created_on')

class ClientRequestCreateView ( LoginRequiredMixin, CreateView ):
    model = ClientRequest
    fields = [
        'category', 
        'detail',
        'client',
        'server',
        'requester',
        'required_date',
    ]

# class RestaurantDetailView ( LoginRequiredMixin, DetailView ):
#     model = ClientRequest
#     template_name = 'companies/restaurant_detail2.html'
#     # context_object_name = 'restaurant'
#     # fields = [
#     #     'short_name', 
#     #     'full_name',
#     #     'image',
#     #     'phone',
#     #     'division',
#     #     'latitude',
#     #     'longitude',
#     #     'is_active',
#     #     'unit_number',
#     #     'street',
#     #     'city',
#     #     'postal_code', 
#     #     'staffs',
#     #     'registered_on',
#     #     'approved_on',
#     # ]

# class RestaurantUpdateView ( LoginRequiredMixin, UserPassesTestMixin, UpdateView ):
#     model = Restaurant
#     fields = [
#         'short_name', 
#         'full_name',
#         'image',
#         'phone',
#         'division',
#         'latitude',
#         'longitude',
#         'is_active',
#         'unit_number',
#         'street',
#         'city',
#         'postal_code', 
#         # 'staffs',
#         # 'registered_on',
#         'approved_on',
#     ]
#     def test_func(self):
#         # restaurant = self.get_object()
#         # if self.request.user == 'admin':
#         #     return True
#         return True

# class RestaurantImageUpdateView ( LoginRequiredMixin, UserPassesTestMixin, UpdateView ):
#     model = Restaurant
#     fields = [
#         'image',
#     ]
#     def test_func(self):
#         # restaurant = self.get_object()
#         # if self.request.user == 'admin':
#         #     return True
#         return True
# # class OilCollectorListView ( ListView ):
# #     model = Restaurant
