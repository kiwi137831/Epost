from django.db import models
from account.models import user

import django.utils.timezone as timezone
# Create your models here.


class order(models.Model):
    order_id = models.CharField(max_length = 10, primary_key= True, default= '0')
    date = models.DateTimeField(default = timezone.now)
    track_id = models.CharField(max_length=20)
    r_address = models.CharField(max_length=50)
    s_address = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    r_phone = models.CharField(max_length=20)
    s_phone = models.CharField(max_length=20)
    receiver = models.CharField(max_length=20)
   # sender = models.ForeignKey(user, to_field='user_id', on_delete=models.CASCADE)
    sender = models.CharField(max_length=20)
    weight = models.CharField(max_length=20)
    s_postcode = models.CharField(max_length=20)
    r_postcode = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    box_id = models.CharField(max_length=20)
    company_id = models.CharField(max_length=20)
    delivery_staff = models.CharField(max_length=20)

