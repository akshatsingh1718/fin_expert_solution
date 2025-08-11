from django.shortcuts import render

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