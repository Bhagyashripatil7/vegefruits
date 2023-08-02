from django.db import models
from django.db import models
class Statement(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    address=models.TextField()
    items=models.CharField(max_length=80)
    total=models.IntegerField()
    modepayment=models.CharField(max_length=50)
    class Meta:
        db_table = "Statement"


# Create your models here.
