from django.shortcuts import render, redirect
from django.http import Http404
import os
from django.conf import settings
from django.contrib import messages
from finance.utils.email import EmailSender, send_email_to_admin
email_sender = EmailSender()

def index(request):
    """Home page view"""
    return render(request, 'finance/index.html')

def about(request):
    """About page view"""
    return render(request, 'finance/about.html')

def contact(request):
    """Contact page view with form handling"""
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message_content = request.POST.get('message')
        
        # Send email using EmailSender class
        try:
            email_sender.send_email_to_admin(name, email, subject, message_content)
            messages.success(request, "Your message has been sent successfully. We'll get back to you soon!")
            return redirect('finance:contact')
        except Exception as e:
            messages.error(request, f"Failed to send message. Please try again later")
    
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
