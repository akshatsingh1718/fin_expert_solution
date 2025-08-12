from django.shortcuts import render
from django.http import Http404
import os
from django.conf import settings

def index(request):
    """Home page view"""
    return render(request, 'finance/index.html')

def about(request):
    """About page view"""
    return render(request, 'finance/about.html')

def contact(request):
    """Contact page view"""
    return render(request, 'finance/contact.html')

def feature(request):
    """Feature page view"""
    return render(request, 'finance/feature.html')

def service(request):
    """Service page view"""
    return render(request, 'finance/service.html')

def team(request):
    """Team page view"""
    return render(request, 'finance/team.html')

def testimonial(request):
    """Testimonial page view"""
    return render(request, 'finance/testimonial.html')

def project(request):
    """Project page view"""
    return render(request, 'finance/project.html')

def service_detail(request, service_name):
    """Dynamic view to handle all service pages"""
    # Define valid service names that correspond to HTML files
    valid_services = [
        'salaried-personal-loan',
        'self-employed-business-loan', 
        'home-loan',
        'loan-against-property',
        'debt-consolidation',
        'used-car-loan',
        'car-refinancing',
        'overdraft-facility'
    ]
    
    # Check if the requested service is valid
    if service_name not in valid_services:
        raise Http404("Service not found")
    
    # Construct template path
    template_path = f'finance/services/{service_name}.html'
    
    # Check if template file exists
    template_full_path = os.path.join(settings.BASE_DIR, 'templates', template_path)
    if not os.path.exists(template_full_path):
        raise Http404("Service page not found")
    
    return render(request, template_path)