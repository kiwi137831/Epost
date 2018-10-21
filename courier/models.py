from django.db import models


class company(models.Model):
    company_id = models.CharField(max_length=10, primary_key=True, default='1')
    name = models.CharField(max_length=20, default='0')
    phone = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    address =models.CharField(max_length=200,default='')
