from django.shortcuts import render
from apps.product.models import Product



def frontpage(request):
    newest_products = Product.objects.all()[0:8] #call the products from the db and slice to get 8 of them
    
    return render(request,'core/frontpage.html', {'newest_products':newest_products}) #to be available in the front 

def contact(request):
    return render(request,'core/contact.html')
    
