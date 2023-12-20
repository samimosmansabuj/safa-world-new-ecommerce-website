from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import Customer
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
import uuid
import random
import os

# Create your views here.
@login_required
def my_account(request):
    user = request.user
    if user.is_customer == False:
        logout(request)
        return redirect('login')
    
    customer = Customer.objects.get(username=user)
    return render(request, 'account/my_account/my_account.html', {'customer': customer})

def track_order(request):
    return render(request, 'account/my_account/track_order.html')

@login_required
def my_order(request):
    return render(request, 'account/my_account/my_order.html')

@login_required
def edit_my_account(request, id):
    customer = Customer.objects.get(id=id)
    context = {'customer': customer}
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        date_of_birth = request.POST['date_of_birth']
        gender = request.POST['gender']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        profile_picture = request.FILES.get('profile_picture')
        
        customer.first_name=first_name
        customer.last_name=last_name
        customer.gender=gender
        customer.email=email
        customer.phone_number=phone_number
        
        if date_of_birth:
            customer.date_of_birth=date_of_birth
        if profile_picture:
            try:
                if customer.profile_picture:
                    os.remove(customer.profile_picture.path)
                customer.profile_picture = profile_picture
            except:
                customer.profile_picture = profile_picture
        customer.save()
        return redirect(request.META['HTTP_REFERER'])
        
    return render(request, 'account/my_account/edit_my_account.html', context)

@login_required
def order_details(request):
    return render(request, 'account/my_account//order_details.html')





def Logout(request):
    logout(request)
    return redirect('home')


def Login(request):
    if request.user.is_authenticated:
        return redirect('my_account')
    form = LoginForm()
    if request.method == 'POST':
        data = LoginForm(request.POST)
        print(data)
        username = data.cleaned_data['username']
        password = data.cleaned_data['password']
        if not Customer.objects.filter(username=username).exists():
            messages.warning(request, 'Username Invalid or Username is not exists')
            return redirect(request.META['HTTP_REFERER'])
        
        customer = Customer.objects.get(username=username)
        if customer.is_verified == False:
            messages.warning(request, "Your Account is not Varify!")
            return redirect('login')
        
        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('my_account')
        else:
            messages.warning(request, 'Wrong Password!')
            return redirect(request.META['HTTP_REFERER'])
        
    return render(request, 'account/login.html', {'form': form})



def registration(request):
    if request.user.is_authenticated:
        return redirect('my_account')
    form = CustomerRegistration()
    if request.method == 'POST':
        form = CustomerRegistration(request.POST)
        print(form)
        password = form.cleaned_data['password']
        if form.is_valid():
            auth_token = uuid.uuid4()
            otp_token = random.randint(111111, 999999)
            user = form.save()
            user.set_password(password)
            user.auth_token = auth_token
            user.otp_token = otp_token
            user.is_customer = True
            user.save()
            send_mail_registration(user.email, auth_token, otp_token, user.id)
            return redirect('otp_verify_account', id=user.id)  
        else:
            messages.warning(request, "Wrong Input! Please Try Again...")
            return redirect(request.META['HTTP_REFERER'])
    return render(request, 'account/registration.html', {'form': form})


def send_mail_registration(email, auth_token, otp_token, id):
    subject = "Account Verficiation Mail!"
    message = f"""Dear User
    Your OTP is: {otp_token}
    or
    Visit This link for verify your account: http://127.0.0.1:8000/token-verify-account/{id}/{auth_token}
    """
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)


def token_verify_account(request, id, auth_token):
    try:
        customer = Customer.objects.get(id=id)
        if customer.is_verified == True:
            messages.success(request, "Your account already verified!")
            return redirect('login')
        
        if customer.auth_token == auth_token:
            customer.is_verified = True
            customer.auth_token = None
            customer.otp_token = None
            customer.save()
            messages.success(request, "Account Verification Successfully!")
            return redirect('login')
        else:
            messages.warning(request, "Wrong Token Input! Please Try Again...")
            return redirect('registration')
    except:
        return render(request, 'base/404.html')

def otp_verify_account(request, id):
    try:
        customer = Customer.objects.get(id=id)
        if customer.is_verified == True:
            messages.success(request, "Your account already verified!")
            return redirect('login')
        
        context = {'customer': customer}
        if request.method == 'POST':
            otp_token = request.POST['otp_token']
            if customer.otp_token == otp_token:
                customer.is_verified = True
                customer.auth_token = None
                customer.otp_token = None
                customer.save()
                messages.success(request, "Account Verification Successfully!")
                return redirect('login')
            else:
                messages.warning(request, "OTP Does Not Match! Please Try Again...")
                return redirect(request.META['HTTP_REFERER'])
        return render(request, 'account/account_verify.html', context)
    except:
        return render(request, 'base/404.html')




def forget_password(request):
    if request.user.is_authenticated:
        return redirect('my_account')
    return render(request, 'account/forget_password.html')

def change_password(request):
    return render(request, 'account/change_password.html')


