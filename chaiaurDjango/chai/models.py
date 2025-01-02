from django.db import models
from django.utils import timezone


# Create your models here.
#  create a table 
    #  check docs sqlite
    # restrict type  use enum 
class chaiVariety(models.Model):
    CHAI_TYPE_CHOICE =  [
        ("ML", "MASALA"),
        ("GR", "GINGER"),
        ("KL", "KIVI"),
        ("PL", "PLAIN"),
        ("EL", "ELAICHI"),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    #  not support directly 
    # required 3rd party plug-in (Pillow)
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default="")
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name