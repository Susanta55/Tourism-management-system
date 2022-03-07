from importlib.resources import Package
from django.shortcuts import get_object_or_404, render
from packages.models import package
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from .models import package

# Create your views here.

def packages(request):
    main_packages = package.objects.order_by('-created_date')
    paginator = Paginator(main_packages,2)
    page = request.GET.get('page')
    paged_packages = paginator.get_page(page)
    data2 = {
        'main_packages' : paged_packages
    }
    return render(request, 'packages/packages.html',data2)


def package_detail(request, id):
    single_package = get_object_or_404(package,pk=id)
    data={
        'single_package': single_package
    }
    return render(request,'packages/package_detail.html',data)
