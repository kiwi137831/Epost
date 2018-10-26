from django.contrib import admin

# Register your models here.
from account.models import user, rate

admin.site.register(rate)
admin.site.register(user)
