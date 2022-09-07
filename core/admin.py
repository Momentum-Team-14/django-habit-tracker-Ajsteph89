from django.contrib import admin
from .models import CustomUser, DailyRecord, Habit
from django.contrib.auth.admin import UserAdmin

# Register your models here.


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Habit)
admin.site.register(DailyRecord)