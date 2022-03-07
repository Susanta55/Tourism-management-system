from django.shortcuts import render

from packages.models import package

def home(request):
    featured_packages = package.objects.order_by('-created_date').filter(is_featured=True)
    data = {
        'featured_packages' : featured_packages
    }
    return render(request, 'pages/home.html',data)
