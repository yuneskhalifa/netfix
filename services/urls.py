from django.urls import path
from . import views as v

urlpatterns = [
    path('list/', v.service_list, name='services_list'),
    path('create/', v.create, name='services_create'),
    path('<int:id>', v.index, name='index'),
    path('services/<int:service_id>/request_service/', v.request_service, name='request_service'),

    # path('<slug:field>/', v.service_field, name='services_field'),
    path('singleService/<int:service_id>/',v.single_service,name='single_service'),
    path('topServices/',v.topServices, name='top_services'),
    path('services/<str:category_name>/', v.services_by_category, name='services_by_category'),
    
     
    

]
