from django.conf.urls import url
from django.urls import path,re_path

from courier import views
import courier
app_name = 'courier'

urlpatterns = [
  #  url(r'^CourierHomepage/$', views.homepage, name='CourierHomepage'),

    path('<str:courier_id>/CourierHomepage/', views.homepage, name='CourierHomepage'),

    path('<str:courier_id>/CourierPickuplists/', views.cpickuplist, name='CourierPickUpLists'),
 #   url(r'^CourierPickuplists/$', views.pickuplist, name='CourierPickUpLists'),

    path('<str:courier_id>/CourierStoreParcels/', views.storepage, name='CourierStoreParcels'),

    #url(r'^CourierStoreParcels/$', views.storepage, name='CourierStoreParcels'),



    path('<str:courier_id>/store/successful/<str:order_id>/', views.cpickup, name ='successfulpage'),


    path('issuereport/<str:order_id>/', views.issuereport, name='issuereport'),

    path('<str:courier_id>/CourierStoreParcels/storeinfo/', views.storeinfo, name='storeinfo'),

   # url(r' CourierStoreParcels/storeinfo', views.storeinfo, name="storeinfo"),
    path('<str:courier_id>/confirm/<str:order_id>/', views.confirmparcel, name ='confirmpage'),
]