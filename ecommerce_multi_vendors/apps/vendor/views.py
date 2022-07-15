
from django.contrib.auth import login 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm #for the form creation 
from django.shortcuts import render, redirect
from .models import Vendor #import database

def become_vendor(request):
    if request.method == 'POST': #check if the form has been submitted
        form = UserCreationForm(request.POST) #instance of the user creation form 
        
        if form.is_valid():
            user = form.save()
            
            login(request, user) #user created here 
            
            vendor = Vendor.objects.create(name=user.username, created_by=user)#reference the object user for the database
            
        return redirect('frontpage') #return the user to the frontpage
        
    else:
        form = UserCreationForm()
         
    return render(request,'vendor/become_vendor.html', {'form':form}) #to see in the templates

@login_required #check if the user is logged
def vendor_admin(request):
    vendor = request.user.vendor
    
    return render(request, 'vendor/vendor_admin.html', {'vendor':vendor})