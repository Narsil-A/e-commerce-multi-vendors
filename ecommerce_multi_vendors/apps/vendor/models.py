from django.contrib.auth.models import User #import models from django, user object
from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=255) #name for the vendor 
    created_at = models.DateTimeField(auto_now_add=True) #check when the user is created, and will be automated
    created_by = models.OneToOneField(User, related_name='vendor', on_delete=models.CASCADE) #reference the user with the vendor created
                                                                                             #only one user can have one vendor    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name  #string representations of the object

    