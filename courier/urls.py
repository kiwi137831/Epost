from django.conf.urls import url
from django.urls import path,re_path

from courier import views
import courier
app_name = 'courier'

urlpatterns = [
    url(r'^CourierHomepage/$', views.homepage, name='CourierHomepage'),
    url(r'^CourierPickuplists/$', views.pickuplist, name='CourierPickUpLists'),
    url(r'^CourierStoreParcels/$', views.storepage, name='CourierStoreParcels'),
    path('lists/successful/<str:order_id>/', views.pickup, name ='successfulpage'),
    path('/issuereport/<str:order_id>/', views.issuereport, name='issuereport'),
    url(r'CourierStoreParcels/storelist', views.storelist, name="storelist")
]