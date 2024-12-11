from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import  UserLoginForm, CustomerSignUpForm, CompanySignUpForm
from .models import User, Company, Customer
from services.models import ServiceRequest, Service
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404
from .models import User


def register(request):
    return render(request, 'users/register.html')


class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'users/register_customer.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        print("Saved email to database:", user.email)  # Debugging line
        login(self.request, user,backend = 'users.auth_backends.EmailBackend')
        return redirect('/')


class CompanySignUpView(CreateView):
    
    model = User
    form_class = CompanySignUpForm
    template_name = 'users/register_company.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'company'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user,backend = 'users.auth_backends.EmailBackend')
        return redirect('/')



def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            # Access the cleaned email and password
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            print("Email:", email)
            print("Password:", password)

            # Authenticate user (you can use a custom backend here)
            user = authenticate(request, email=email, password=password)
            if user:
                #user.backend = 'users.backends.EmailBackend'
                login(request, user, backend = 'users.auth_backends.EmailBackend')
                messages.success(request, 'Do you want to login with diffrent user?')
                return redirect('services_list')
            else:
                messages.error(request, 'Invalid email or password.') 
                return render(request, 'users/login.html', {'form': form})
    else:
        form = UserLoginForm()
    
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)  # Logs the user out and clears the session
    return redirect('/logout')  # Redirect to the homepage or login page



@login_required
def profile_view(request):
    return render(request, 'users/profile.html', {})



    

def profile_single_view(request, user_id):
    # Fetch the User object by ID or return a 404 if not found
    user = get_object_or_404(User, id=user_id)
    

    # Initialize user_requests variable outside the if condition to ensure it exists in both branches
    user_requests = []
    services = []
    if request.user.is_authenticated:
        if user.is_customer:
        # Get service requests for the customer
            user_requests = ServiceRequest.objects.filter(customer=request.user.customer)
            for request1 in user_requests:
                request1.total_cost = request1.service.price_hour * request1.duration
        
        elif user.is_company:
        # Get services for the company
            services = Service.objects.filter(company=request.user.company)

    # Now `user_requests` will always exist
    return render(request, 'users/profile.html', {'user': user, 'user_requests': user_requests, 'services': services})

    # Render the profile page with the user object




