from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import customer
from core.forms import CustomerForm

# Create your views here.

def auth_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).first():
            messages.error(request, 'user not found, try with a valid username')
            return redirect('Login')
        
        valid_user = authenticate(request, username = username, password = password)
        if not valid_user:
            messages.error(request, 'Invalid login credential, please check!!')
            return redirect('Login')
        
        login(request, valid_user)
        return redirect('Dashboard')
    
    return render(request,'Auth/login.html')

@login_required(login_url='Login')
def dashboard(request):
    total_customer = customer.objects.all().filter(from_user = request.user).count()
    account_approved = customer.objects.all().filter(from_user = request.user) & customer.objects.all().filter(account_status = True)
    account_pending = customer.objects.all().filter(from_user = request.user) & customer.objects.all().filter(account_status = False)
    context = {
        'total_customer':total_customer,
        'account_approved':account_approved.count(),
        'account_pending':account_pending.count(),
    }
    return render(request, 'User/dashboard.html', context)

def auth_logout(request):
    logout(request)
    messages.success(request, 'Thanks for spending some time with us :)')
    return redirect('Login')

@login_required(login_url='Login')
def add_customer(request):
    if request.method == "POST":
        from_user = request.user
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        married_status = request.POST.get('married_status')
        nominee = request.POST.get('nominee')
        aadhar = request.POST.get('aadhar')
        pan = request.POST.get('pan')
        address = request.POST.get('address')
        pin = request.POST.get('pin')
        pan_image = request.FILES.get('pan_image')
        passport_image = request.FILES.get('passport_image')
        aadhar_front_image = request.FILES.get('aadhar_front_image')
        aadhar_back_image = request.FILES.get('aadhar_back_image')
        signeture_image = request.FILES.get('signeture_image')

        if customer.objects.filter(mobile = mobile).first():
            messages.error(request, 'Mobile number already exist, go with a diffrent one !!')
            return redirect('Add_customer')
        
        if customer.objects.filter(aadhar = aadhar).first():
            messages.error(request, 'Aadhar number already exist, go with a diffrent one !!')
            return redirect('Add_customer')
        
        if customer.objects.filter(pan = pan).first():
            messages.error(request, 'Pan number already exist, go with a diffrent one !!')
            return redirect('Add_customer')
        
        customer_obj = customer(from_user=from_user, name=name, dob=dob, mobile=mobile, email=email, father_name=father_name, mother_name=mother_name, married_status=married_status, nominee=nominee, aadhar=aadhar, pan=pan, address=address, pin=pin, pan_image=pan_image, passport_image=passport_image, aadhar_front_image=aadhar_front_image, aadhar_back_image=aadhar_back_image, signeture_image=signeture_image)
        customer_obj.save()
        messages.success(request, f'Customer {name} | data submitted successfully')
        return redirect('Add_customer')


    return render(request,'User/addcustomer.html')

@login_required(login_url='Login')
def all_customers(request):
    user = request.user
    customer_obj = customer.objects.all().filter(from_user = user).order_by('-created_at')
    return render(request, 'User/allcustomers.html', {'customers':customer_obj})

@login_required(login_url='Login')
def view_customer(request, slug):
    customer_obj = customer.objects.get(customer_id = slug)
    return render(request, 'User/viewcustomer.html', {'customers':customer_obj})

@login_required(login_url='Login')
def delete_customer(request, slug):
    customer_obj = customer.objects.get(customer_id = slug)
    customer_obj.delete()
    messages.success(request, f'{id} user is deleted successfully')
    return redirect('Dashboard')


def update_customer(request, slug):
    instance = customer.objects.get(customer_id = slug)
    
    if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES, instance = instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Welldone, Data successfully Updated.....')
            return redirect('Customers')
    else:
        form = CustomerForm(instance=instance)

    context = {
        'form':form,
        'customer_obj':instance,
    }

    return render(request, 'User/customerupdate.html', context)

def Banks_Cards(request):
    return render(request, 'User/banks-cards.html')