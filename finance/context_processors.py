"""
Context processors for the finance app.
This file contains functions that add variables to the template context globally.
"""

def site_settings(request):
    """
    Add site-wide settings to template context.
    These variables will be available in all templates.
    """
    return {
        # Company Information
        'COMPANY_NAME': 'Fin Expert Solution',
        'COMPANY_TAGLINE': 'Financial Services Website Template',
        'COMPANY_DESCRIPTION': 'Your trusted partner for comprehensive financial services and solutions.',
        
        # Contact Information
        'COMPANY_ADDRESS': 'Suyash Plaza CHS Ltd,  office - 404, Kalyan West, Thane,  Maharashtra,  Pin- 421301',
        'COMPANY_PHONE': '+91 9999999999',
        'COMPANY_EMAIL': 'info@finxpertsolution.com',
        'COMPANY_HOURS': '9.00 am - 9.00 pm',
        
        # Social Media Links
        'SOCIAL_FACEBOOK': 'https://facebook.com/finanza',
        'SOCIAL_TWITTER': 'https://twitter.com/finanza',
        'SOCIAL_LINKEDIN': 'https://linkedin.com/company/finanza',
        'SOCIAL_YOUTUBE': 'https://youtube.com/finanza',
        
        # Website Information
        'SITE_URL': 'https://finxpertsolution.com',
        'COPYRIGHT_YEAR': '2024',
        'COPYRIGHT_TEXT': 'All Rights Reserved',
        
        # Services List
        'MAIN_SERVICES': [
            'Financial Planning',
            'Cash Investment', 
            'Financial Consultancy',
            'Business Loans',
            'Business Analysis',
            'Marketing Research'
        ],
        
        # Quick Links
        'QUICK_LINKS': [
            {'name': 'About Us', 'url': 'finance:about'},
            {'name': 'Contact Us', 'url': 'finance:contact'},
            {'name': 'Our Services', 'url': 'finance:service'},
            {'name': 'Terms & Condition', 'url': '#'},
            {'name': 'Support', 'url': '#'},
        ]
    }
