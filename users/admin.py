from django.contrib import admin

from .models import User, Customer, Company
from .models import Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email")


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("user", "field")


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("user", "birth")




@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user",)
