from django.conf.urls import url, include
from django.urls import path,re_path
from customer import views
import  customer
app_name = 'customer'
urlpatterns = [

    url(r'^homepage/$', views.homepage, name='homepage'),
    url(r'^lists/$', views.pickuplist, name='PickUpList'),
  #  url(r'^lists/successful/(?P<order>\d+)$', views.pickup, name='successfulpage'),
    path('/issuereport/<str:order_id>/', views.issuereport, name='issuereport'),
    path('lists/successful/<str:order_id>/', views.pickup, name ='successfulpage'),
]