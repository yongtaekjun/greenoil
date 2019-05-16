from django.contrib import admin

from .models import UserProfile, UserInfoChangedLog
# from .models import UserRole

admin.site.register(UserProfile)
# admin.site.register(UserRole)
admin.site.register(UserInfoChangedLog)
