from django.db import models
from django.urls import reverse

# Create your models here.

class WishList(models.Model):
    Description = models.TextField(max_length=300)
    
    def __str__(self):
        return self.item
    
    def get_absolute_url(self):
        return reverse('index')