from django.db import models
import django.utils.timezone as timezone


class company(models.Model):
    company_id = models.CharField(max_length=10, primary_key=True, default='1')
    name = models.CharField(max_length=20, default='0')
    phone = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    address =models.CharField(max_length=200,default='')
class issue (models.Model):
    issue_id = models.CharField(max_length = 10, primary_key= True, default= '1')
    order_id = models.CharField(max_length=20, default= '0')
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=200)
    date = models.DateTimeField(default = timezone.now)
    status = models.CharField(max_length=20, default= 'wait')
