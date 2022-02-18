from django.shortcuts import render

# Create your views here.

def packages(request):
    return render(request, 'packages/packages.html')