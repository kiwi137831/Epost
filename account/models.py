from django.db import models

# Create your models here.



class user(models.Model):
    user_id = models.CharField(max_length = 10, primary_key= True, default= '0')
    account = models.CharField(max_length=20, default = 'Check')
    password = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    address =models.CharField(max_length=50)
    gender = models.CharField(max_length=5)
    age = models.CharField(max_length=5)
