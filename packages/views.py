
from importlib.resources import Package
from django.shortcuts import get_object_or_404, redirect, render
from packages.models import package
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from .models import package,booking_tour
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def packages(request):
    main_packages = package.objects.order_by('-created_date')
    dest_search = package.objects.values_list('destination', flat=True).distinct()
    loc_search = package.objects.values_list('location', flat=True).distinct()
    acti_search = package.objects.values_list('activities', flat=True).distinct()
    price_search = package.objects.values_list('price', flat=True).distinct()
    paginator = Paginator(main_packages,2)
    page = request.GET.get('page')
    paged_packages = paginator.get_page(page)
    data2 = {
        'main_packages' : paged_packages,
        'dest_search' : dest_search,
        'loc_search' : loc_search,
        'acti_search' : acti_search,
        'price_search' : price_search,

    }
    return render(request, 'packages/packages.html',data2)


def package_detail(request, slug):
    single_package = get_object_or_404(package,slug=slug)
    data={
        'single_package': single_package
    }
    return render(request,'packages/package_detail.html',data)

@login_required(login_url='login')
def booking(request,slug):
    bookpackage = get_object_or_404(package,slug=slug)
    data = {
        'tour':bookpackage
    }
    
    if request.method == 'POST':
        context = {'has_error': False}
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        persons = request.POST.get('persons')
        country= request.POST.get('country')
        email= request.POST.get('email')
        trip_name = request.POST.get('trip_name')
        price = request.POST.get('price')
        mobile= request.POST.get('mobile')
        arrival_date= request.POST.get('arrival_date')
        departure_date= request.POST.get('departure_date')
        comments = request.POST.get('comments')

        if booking_tour.objects.filter(mobile=mobile).exists():
            messages.add_message(request,messages.ERROR,
                                                    'mobile already exists')
            context['has_error'] = True                                         
            
        
        if booking_tour.objects.filter(email=email).exists():
            messages.add_message(request,messages.ERROR,
                                                    'Email already exists')
            context['has_error'] = True 

        if context['has_error']:
            return render(request, 'packages/booking.html')                                            
            

        booked = booking_tour.objects.create(firstname=firstname,lastname=lastname,persons=persons,country=country,mobile=mobile,trip_name=trip_name,email=email,price=price,arrival_date=arrival_date, departure_date=departure_date,comments=comments)
        booked.save()
        id = booked.id

        return redirect('checkout/'+str(id))
        
    

        


    
    return render(request, 'packages/booking.html',data)  

def search(request):
    packages = package.objects.order_by('-created_date')
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            packages = packages.filter(description__icontains=keyword)
            

    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            packages = packages.filter(location__iexact=location)        
    
    if 'destination' in request.GET:
        destination = request.GET['destination']
        if destination:
            packages = packages.filter(destination__iexact=destination)   

    if 'activities' in request.GET:
        activities = request.GET['activities']
        if activities:
            packages = packages.filter(activities__iexact=activities)                     

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            packages = packages.filter(price__iexact=price)        

    data= {
        'packages': packages
    }
    return render(request, 'packages/search.html',data)      

def checkout(request,id):
    check_tour = get_object_or_404(booking_tour,id=id)
    data = {
        'check':check_tour
    }
    
   
    return render(request, 'packages/checkout.html',data)

def success(request,id):
    check_tour = get_object_or_404(booking_tour,id=id)
    data = {
        'check':check_tour
    }
    check_tour.is_paid = True
    check_tour.save()
    return render(request,'packages/success.html')

def error_404(request,exception):
    return render(request,'pages/pagenotfound.html')    