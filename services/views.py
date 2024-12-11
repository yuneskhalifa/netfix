from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect

from users.models import Company, Customer, User

from .models import Service, ServiceRequest
from .forms import CreateNewService, RequestServiceForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render
from .models import Service


def service_list(request):
    services = Service.objects.all().order_by("-date")
    print("Services:", services)
    return render(request, 'services/list.html', {'services': services})


def index(request, id):
    service = Service.objects.get(id=id)
    return render(request, 'services/single_service.html', {'service': service})


def create(request):
    if request.method == 'POST':
        form = CreateNewService(data=request.POST)
        if form.is_valid():
            try:
                # Ensure the user is authenticated and is a company
                if request.user.is_authenticated and request.user.is_company:
                    company = get_object_or_404(Company, user=request.user)
                    if company.field == 'All in One':
                        field_value = form.cleaned_data['field']
                    else:
                        # Default to the company's field if it is specific (e.g., 'Carpentry')
                        field_value = company.field
                    service = Service(
                        company=company,
                        name=form.cleaned_data['name'],
                        description=form.cleaned_data['description'],
                        price_hour=form.cleaned_data['price_hour'],
                        field=field_value,
                    )
                    service.save()
                    return redirect('services_list')
                else:
                    print("User is not authenticated or not a company.")
            except Company.DoesNotExist:
                print("Company not found for the user.")
        else:
            print("Form is not valid.")
    else:
        visible = True 
        if request.user.is_authenticated and request.user.is_company:
            company = get_object_or_404(Company, user=request.user)
            if company.field != 'All in One':
                visible = False

        form = CreateNewService(visible = visible)

    return render(request, 'services/create.html', {'form': form})



from django.shortcuts import render, redirect
from .forms import RequestServiceForm

from django.shortcuts import get_object_or_404, redirect, render



@login_required
def request_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    

    if request.method == 'POST':
        form = RequestServiceForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = Customer.objects.get(user=request.user)  # Set the requesting user
            service_request.service = service  # Set the selected service
            service_request.save()
            return redirect('singleProfile', user_id=request.user.id)
    else:
        form = RequestServiceForm(initial={'service': service})

    return render(request, 'services/request_service.html', {'form': form, 'service': service})





def single_service(request, service_id):
    # Fetch the User object by ID or return a 404 if not found
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'services/single_service.html', {'service': service})




def topServices(request):
    most_requested_services = Service.objects.annotate(request_count=Count('requests')).order_by('-request_count')
    
    # Render a template for most requested services
    return render(request, 'services/top_services.html', {'most_requested_services': most_requested_services})


def services_by_category(request, category_name):
    # Fetch services for the selected category
    services = Service.objects.filter(field=category_name)

    return render(request, 'services/services_by_category.html', {
        'services': services,
        'category_name': category_name
    })

    
    



