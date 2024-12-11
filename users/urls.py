from django.urls import path
from django.contrib.auth import views

from  .views import login_view, CompanySignUpView, register, CustomerSignUpView, logout_view, profile_view, profile_single_view

urlpatterns = [
    path('', register, name='register'),
    path('company/', CompanySignUpView.as_view(), name='register_company'),
    path('customer/', CustomerSignUpView.as_view(), name='register_customer'),
    path('login', login_view, name='login_user'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('singleProfile/<int:user_id>/', profile_single_view, name='singleProfile')
]
