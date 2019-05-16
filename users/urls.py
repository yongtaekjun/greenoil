
from . import views as user_views
from django.contrib.auth import views as auth_views

from django.urls import path

urlpatterns = [
    # path('list/', users_views.list_view, name='user-list' ),
    path('users/register/', user_views.register, name='users_register' ),
    path('users/profile/', user_views.user_profile, name='users_profile'),
    path('users/login/', auth_views.LoginView.as_view( template_name = 'users/login.html'), name='users_login' ),
    path('users/logout/', auth_views.LogoutView.as_view( template_name = 'users/logout.html'), name='users_logout' ),
]
