from datetime import datetime
from distutils.command.upload import upload
from django.db import models

# Create your models here.


acti_choice =(
    ('Tour','Tour'),
    ('Trekking','Trekking'),
    ('Sight seeing','Sight seeing'),
    ('Jungle safari', 'Jungle safari'),
    ('mountaineering', 'mountaineering'),

)

class package(models.Model):
    destination = models.CharField(max_length=200)
    price = models.IntegerField()
    description= models.TextField(max_length=1000)
    location = models.CharField(max_length=200)
    duration = models.IntegerField()
    package_img= models.ImageField(upload_to='photos/', blank=True)
    max_size = models.IntegerField()
    transport = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    activities = models.CharField(choices=acti_choice, max_length=200)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self) :
        return self.destination


