from django.db import models
import django.utils.timezone as timezone
# Create your models here.



class user(models.Model):
    user_id = models.CharField(max_length = 10, primary_key= True, default= '2')
    account = models.CharField(max_length=20, default = 'Check')
    password = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    age = models.CharField(max_length=5)
    type = models.CharField(max_length=10,default= '0')
    gender = models.CharField(max_length=10,default= '0')

class courier(models.Model):
    courier_id = models.CharField(max_length = 10, primary_key= True, default= '1')
    account = models.CharField(max_length=20, default = 'Check')
    password = models.CharField(max_length=10,default='0')
    name = models.CharField(max_length=10,default='0')
    company_id= models.CharField(max_length=10,default= '0')
    phone = models.CharField(max_length=50,default='0')
    gender = models.CharField(max_length=10,default='0')
    age = models.CharField(max_length=5,default='0')


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
    #updated = models.DateTimeField(auto_now=True)
    #status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title