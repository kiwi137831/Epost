from django.contrib import admin


# Register your models here.
from customer.models import issues, order

admin.site.register(issues)
admin.site.register(order)
