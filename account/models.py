from django.db import models
from django.utils import timezone
from django.contrib.auth.models import UserManager
import win32timezone

class notice(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    notice_id = models.CharField(max_length=10, primary_key=True, default='0')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    #author = models.ForeignKey(user,on_delete=models.CASCADE)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    #created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title


class user(models.Model):
    user_id = models.CharField(max_length = 10, primary_key= True, default= '0')
    account = models.CharField(max_length=20, default = 'Check')
    password = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    type = (('customer', 'Customer'),
            ('courier', 'Courier'))
    career = models.CharField(choices=type, max_length=32, default='customer', verbose_name='career')
    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    gender = (('male','Male'),
              ('female','Female'))
    sex = models.CharField(choices=gender, max_length=32, default='man', verbose_name='gender')
    age = models.CharField(max_length=5)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'user'

#class UserProfile(models.Model):
    #Puser = models.OneToOneField(user,unique=True,verbose_name=('user'))
    #Pphone = models.CharField(max_length=20)
    #Pname = models.CharField(max_length=10)
    #Paddress = models.CharField(max_length=50)
    #Page = models.CharField(max_length=5)
    #gender = (('male', 'Male'),
              #('female', 'Female'))
    #Psex = models.CharField(choices=gender, max_length=32, default='man', verbose_name='gender'