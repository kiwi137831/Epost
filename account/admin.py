from django.contrib import admin
from .models import notice

# Register your models here.
#class ArticleAdmin(admin.ModelAdmin):
    #pass
admin.site.register(notice)