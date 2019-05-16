
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from users import views as users_views
from calls import views as calls_views
from companies import views as companies_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),

    # path('users/role/',                     users_views.UserRoleListView.as_view(),  name='role_list'),
    path('companies/roles/',                companies_views.UserRoleListView.as_view(),  name='role_list'),
    path('companies/role/create',           companies_views.UserRoleCreateView.as_view(),  name='role_create'),
    path('companies/contracts/',            companies_views.OilCollectContractListView.as_view(),  name='contract_list'),

    path('restaurant/',                     companies_views.RestaurantListView.as_view(),       name='restaurant_list'),
    path('restaurant/new/',                 companies_views.RestaurantCreateView.as_view(),     name='restaurant_new'),
    # path('restaurant/create/', DON'T USE /create/ It might be registered keyword
    path('restaurant/<str:pk>/',            companies_views.RestaurantDetailView.as_view(),     name='restaurant_detail'),
    path('restaurant/<str:pk>/update/',     companies_views.RestaurantUpdateView.as_view(),     name='restaurant_update'),
    path('restaurant/<str:pk>/update/image',companies_views.RestaurantImageUpdateView.as_view(),name='restaurant_image_update'),

    path('calls/',                          calls_views.ClientRequestListView.as_view(), name='calls_list'),
    path('calls/history',                   calls_views.CallHistoryListView.as_view(), name='history_list'),
    
    path('users/register/',                 users_views.register, name='users_register'),
    path('users/profile/',                  users_views.user_profile, name='users_profile'),
    path('users/login/',                    auth_views.LoginView.as_view(template_name='users/login.html'), name='users_login'),
    path('users/logout/',                   auth_views.LogoutView.as_view(template_name='users/logout.html'), name='users_logout'),
    path('users/password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='users_password_reset'),
    path('users/password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('users/password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('users/password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='users_password_reset_complete'),
    # path('', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)