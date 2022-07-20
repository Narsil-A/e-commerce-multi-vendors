from io import BytesIO
from PIL import Image
from django.core.files import File
from django.db import models
from apps.vendor.models import Vendor #importing vendor models for this app


class Category(models.Model):
    title = models.CharField(max_length=255) 
    slug = models.SlugField() #address version of the name
    ordering = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['ordering'] #ascending order the category,  created a list
        
    def __str__(self):
        return self.title  #string representation of the object

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2) #depended on the currency
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)        
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ('-date_added',) #decending order
         
    def __str__(self):
        return self.title
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'
            
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumbnail = File(thumb_io, name=image.name)
        
        return thumbnail 
   