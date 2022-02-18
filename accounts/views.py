from .utils import generate_token
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from validate_email import validate_email
from accounts.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.




  
                                         


def login_user(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user=authenticate(request, username=username,password=password)
        
        if not user.is_email_verified:
            messages.add_message(request,messages.ERROR,
                                                    'Email is not verified, verify it to login')
            return redirect('login')                                       
            
        if not user:
            messages.add_message(request,messages.ERROR,
                                                    'Invalid username or password')
            return redirect('login')                                       
            
        login(request,user)
        messages.add_message(request,messages.SUCCESS,
                                                    'Logged in successfully')

        return redirect('home')                                            
        
        


    
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        context = {'has_error': False}
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
            

        if len(password) < 6:
            messages.add_message(request,messages.ERROR,
                                                    'Password should be 6 characters')
            context['has_error'] = True                                        
            
        
        if password != confirm_password:
            messages.add_message(request,messages.ERROR,
                                                    'Password mismatch')
            context['has_error'] = True   
               
        if not validate_email(email):
            messages.add_message(request,messages.ERROR,
                                                    'Enter a valid email address')
            context['has_error'] = True

        if not username:
            messages.add_message(request,messages.ERROR,
                                                    'Username is required')
            context['has_error'] = True
        
        if User.objects.filter(username=username).exists():
            messages.add_message(request,messages.ERROR,
                                                    'Username already exists')
            context['has_error'] = True
        
        if User.objects.filter(email=email).exists():
            messages.add_message(request,messages.ERROR,
                                                    'Email already exists')
            context['has_error'] = True

        if context['has_error']:
            return render(request, 'accounts/register.html')


        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()

        send_activate_email(user,request)

        messages.add_message(request,messages.INFO,
                                                    'Check your mail for verification')

        return redirect('register')                                           

        

        
       


    return render(request, 'accounts/register.html')
 

def logout(request):
    return redirect('home')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def send_activate_email(user,request):
    current_site = get_current_site(request)
    email_subject = 'Activate your account'
    email_body = render_to_string('accounts/activate.html',{
        'user':user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)

        


    })
   

    email =EmailMessage(subject=email_subject, body=email_body,
                from_email= settings.EMAIL_HOST_USER,
                to=[user.email]
                )

    email.send()            


def verify(request, id, token):


    try:
        uid = urlsafe_base64_decode(id).decode()

        user = User.objects.get(pk=uid)

    except Exception as e:
        user= None

    if user and generate_token.check_token(user,token):
        user.is_email_verified = True
        user.save()
        print("saved in database")


        messages.add_message(request,messages.SUCCESS,
                                                    'Email is successfully verified')
                                                    
        return redirect('login')  