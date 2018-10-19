from django.db import models
import django.utils.timezone as timezone


# Create your models here.

class user(models.Model):
    user_id = models.CharField(max_length = 10, primary_key= True, default= '0')
    account = models.CharField(max_length=20, default = 'Check')
    password = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    type = models.CharField(max_length=10,default= '0')
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    address =models.CharField(max_length=50)
    gender = models.CharField(max_length=5)
    age = models.CharField(max_length=5)

class rate(models.Model):
    rate_id = models.CharField(max_length = 10, primary_key = True, default='0')
    date = models.DateTimeField(default=timezone.now)
    level = models.CharField(max_length=10)
    content = models.CharField(max_length=100)
    order_id =models.CharField(max_length=10)
    writer_id = models.CharField(max_length=10)
    delivery_id = models.CharField(max_length=10)