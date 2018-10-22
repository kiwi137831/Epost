from django.conf.urls import url, include
from django.urls import path,re_path
from customer import views
import  customer
app_name = 'customer'
urlpatterns = [

    path('<str:user_id>/homepage/', views.homepage, name='homepage'),
    path('<str:user_id>/lists/', views.pickuplist, name='PickUpList'),
  #  url(r'^lists/successful/(?P<order>\d+)$', views.pickup, name='successfulpage'),
    path('<str:user_id>/issuereport/<str:order_id>/', views.issuereport, name='issuereport'),
    path('<str:user_id>/lists/successful/<str:order_id>/', views.pickup, name ='successful'),
    path('<str:user_id>/noticeboard/', views.notice, name ='notice'),
    path('<str:user_id>/express/', views.send, name='express'),
]