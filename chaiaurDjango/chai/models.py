from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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

# study relationships 
#  One to many 
class ChaiReview(models.Model):
    chai = models.ForeignKey(chaiVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    
# Many to Many [store]
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(chaiVariety, related_name='stores')

    def __str__(self):
        return self.name
    
# One to One [1 certificate for 1 student ][unique]

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(chaiVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.name.chai}'

