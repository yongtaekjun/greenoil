# companies/views.py

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Restaurant, UserRole, OilCollectContract
# from users.models import UserRole
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserRoleCreateForm
from django.http    import HttpResponseRedirect


class OilCollectContractListView ( LoginRequiredMixin, UserPassesTestMixin, ListView ):
    model = OilCollectContract
    template_name = 'companies/contract_list.html'
    context_object_name = 'contracts'
    ordering = ['restaurant']
    def test_func(self):
        # roles = self.get_object()
        # if self.request.user == 'admin':
        #     return True
        return True


class UserRoleListView ( LoginRequiredMixin, UserPassesTestMixin, ListView ):
    model = UserRole
    template_name = 'companies/role_list.html'
    context_object_name = 'roles'
    # context_role = 
    ordering = ['user']


    def test_func(self):
        # roles = self.get_object()
        # if self.request.user == 'admin':
        #     return True
        return True

class UserRoleCreateView ( CreateView ):
    model = UserRole
    template_name = 'companies/user_role_create.html'
    fields = ('user', 'company', 'role')
    form = UserRoleCreateForm

    def form_valid (self, form ):
        self.object = form.save ( commit=False )
        self.object.save()

        # category_list = self.request.POST ['st_category_list'].split(',')
        # for category_name in category_list:
        #     Category.objects.create (
        #         project = Project.objects.get ( id=self.object.id ),
        #         name = category_name
        #     ).save()

        return redirect('role_list')


def get_user_role_list ( user ):
    return UserRole.objects.filter ( user = user)

def has_user_role ( user, company, role ):
    try:
        user_role = UserRole.objects.get ( user = user, company = company, role=role )
        return True
    # except UserRole.DoesNotExist():
    except:
        return False

def is_restaurant_staff ( user, restaurant ):
    try:
        user_role = UserRole.objects.get ( user = user, company = restaurant )
        return True
    # except UserRole.DoesNotExist():
    except:
        return False


# def project_detail( request, project_slug ):
#     project = get_object_or_404 ( Project, slug = project_slug)
#     if request.method == 'GET':
#         category_list = Category.objects.filter ( project = project )

#         return render ( 
#             request, 
#             'budget/project_detail.html', 
#             {   'project': project, 
#                 'expense_list': project.expense_list.all(), 
#                 'category_list': category_list,
#             } 
#         )
#     elif request.method == 'POST':
#         form = ExpenseForm ( request.POST )
#         if form.is_valid():
#             title = form.cleaned_data [ 'title' ]
#             amount = form.cleaned_data [ 'amount' ]
#             category_name = form.cleaned_data [ 'category' ]
#             # print ( "'%s'"  % (category_name) )
#             category = get_object_or_404 ( Category, project = project, name__contains = category_name, )
#             # try:
#             #     category = Category.objects.get( project=project, name=category_name,)

#             # except Category.DoesNotExist:
#             #     return render(request, 'budget/error_message.html')

#             Expense.objects.create ( 
#                 project = project,
#                 title = title,
#                 amount = amount,
#                 # category = category,
#                 category = category,
#             ).save()
#     # elif request.method == 'DELETE':
#     #     id = json.load ( request.body ['id'])
#     #     expense = get_object_or_404 ( Expense, id = id)
#     #     expense.delete()

#     return HttpResponseRedirect ( project_slug )

class RestaurantListView ( LoginRequiredMixin, ListView ):
    model = Restaurant
    template_name = 'companies/restaurant_list.html'
    context_object_name = 'restaurants'
    ordering = ['short_name']

class RestaurantCreateView ( LoginRequiredMixin, CreateView ):
    model = Restaurant
    fields = [
        'short_name', 
        'full_name',
        'image',
        'phone',
        'division',
        'latitude',
        'longitude',
        'is_active',
        'unit_number',
        'street',
        'city',
        'postal_code', 
        # 'staffs',
        # 'registered_on',
        'approved_on',
    ]

class RestaurantDetailView ( LoginRequiredMixin, DetailView ):
    model = Restaurant
    template_name = 'companies/restaurant_detail2.html'
    # context_object_name = 'restaurant'
    # fields = [
    #     'short_name', 
    #     'full_name',
    #     'image',
    #     'phone',
    #     'division',
    #     'latitude',
    #     'longitude',
    #     'is_active',
    #     'unit_number',
    #     'street',
    #     'city',
    #     'postal_code', 
    #     'staffs',
    #     'registered_on',
    #     'approved_on',
    # ]

class RestaurantUpdateView ( LoginRequiredMixin, UserPassesTestMixin, UpdateView ):
    model = Restaurant
    fields = [
        'short_name', 
        'full_name',
        'image',
        'phone',
        'division',
        'latitude',
        'longitude',
        'is_active',
        'unit_number',
        'street',
        'city',
        'postal_code', 
        # 'staffs',
        # 'registered_on',
        'approved_on',
    ]
    def test_func(self):
        # restaurant = self.get_object()
        # if self.request.user == 'admin':
        #     return True
        return True

class RestaurantImageUpdateView ( LoginRequiredMixin, UserPassesTestMixin, UpdateView ):
    model = Restaurant
    fields = [
        'image',
    ]
    def test_func(self):
        # restaurant = self.get_object()
        # if self.request.user == 'admin':
        #     return True
        return True
# class OilCollectorListView ( ListView ):
#     model = Restaurant
