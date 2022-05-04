from datetime import datetime
import email
from django.db import models
from django.dispatch import receiver
from django.utils import timezone

from accounts.models import User
from .make_slug import unique_slug_generator
from django.db.models.signals import pre_save

# Create your models here.


acti_choice =(
    ('Tour','Tour'),
    ('Trekking','Trekking'),
    ('Sight seeing','Sight seeing'),
    ('Jungle safari', 'Jungle safari'),
    ('mountaineering', 'mountaineering'),

)

class package(models.Model):
    destination = models.CharField(max_length=200, primary_key=True)
    price = models.IntegerField()
    description= models.TextField(max_length=1000)
    location = models.CharField(max_length=200)
    duration = models.IntegerField()
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    package_img= models.ImageField(upload_to='photos/', blank=True)
    max_size = models.IntegerField()
    transport = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    activities = models.CharField(choices=acti_choice, max_length=200)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self) :
        return self.destination

@receiver(pre_save, sender=package)
def pre_save_receiver(sender, instance, *args, **kwargs):
      if not instance.slug:
          instance.slug = unique_slug_generator(instance)



class booking_tour(models.Model):
    firstname = models.CharField(max_length=200, default='')
    lastname = models.CharField(max_length=200, default='')
    persons = models.CharField(max_length=200, default='')
    country= models.CharField(max_length=200, default='')
    email= models.EmailField(max_length=200, default='')
    mobile= models.CharField(max_length=18,default='')
    trip_name = models.CharField(max_length=200, default='', null=True)
    price = models.IntegerField(default='0')
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    arrival_date= models.DateField(default=timezone.now)
    departure_date= models.DateField(default=timezone.now)
    comments = models.TextField(max_length=1000,blank=True, null=True)
    is_paid = models.BooleanField(default=False)

