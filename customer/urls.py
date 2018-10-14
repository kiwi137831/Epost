from django.conf.urls import url, include

from customer import views
import  customer

urlpatterns = [

    url(r'^homepage/$', views.homepage, name='homepage'),
    url(r'^lists/$', views.pickuplist, name='PickUpList'),
    url(r'^lists/successful/(?P<orderid>\d+)$', views.pickup, name='successfulpage'),


]