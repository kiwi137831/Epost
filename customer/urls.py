from django.conf.urls import url, include

from customer import views
import  customer

urlpatterns = [

    url(r'^homepage/$', views.homepage, name='homepage'),
]