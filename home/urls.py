
from . import views as home_views
from django.urls import path

urlpatterns = [
    path('', home_views.home, name='home_home' ),
    path('about/', home_views.about, name='home_about' ),
]
