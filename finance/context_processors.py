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
        'COMPANY_PHONE': '9819020057',
        'COMPANY_WHATSAPP': '9819020057',
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
        "TESTIMONIALS": [
            {
                "name": "Akshat Singh",
                "profession": "Small Business Owner",
                "text": "Fin Expert Solutions helped us streamline our financial planning and manage cash flow more effectively. Their expert advice gave us the confidence to expand our business without worrying about risks.",
                "image_url": "img/testimonial/akshat.jpeg"
            },
            {
                "name": "Ajay Pandey",
                "profession": "Individual Investor",
                "text": "I was struggling with investment decisions, but their team guided me with clear strategies. Today, my portfolio is growing steadily, and I feel financially secure for the future.",
                "image_url": "img/testimonial/ajay.png"
            },
            {
                "name": "Lakshay Gupta",
                "profession": "Entrepreneur",
                "text": "The consultancy services from Fin Expert Solutions are top-notch. They simplified complex financial terms and gave us practical solutions that actually worked. Highly recommend their expertise.",
                "image_url": "img/testimonial/lakshay.png"
            }
        ]
    }
