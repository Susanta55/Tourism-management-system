from django.shortcuts import render
from pages.models import about,term

from packages.models import package
from django.shortcuts import get_object_or_404

def home(request):
    featured_packages = package.objects.order_by('-created_date').filter(is_featured=True)
    data = {
        'featured_packages' : featured_packages
    }
    return render(request, 'pages/home.html',data)


def pagenotfound(request):
    return render(request,'pages/pagenotfound.html')


def about_us(request):
    about_us = get_object_or_404(about)
    data={
        'about': about_us
    }
    return render(request,'pages/about.html',data)


def terms(request):
    terms_cond = get_object_or_404(term)
    data={
        'terms_con': terms_cond
    }
    return render(request,'pages/terms.html',data)    

def FAQ(request):
    return render(request,'pages/FAQ.html')    