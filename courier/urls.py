from django.conf.urls import url

from courier import views
import courier
app_name = 'courier'

urlpatterns = [
    url(r'^CourierHomepage/$', views.homepage, name='CourierHomepage'),
    url(r'^CourierPickuplists/$', views.pickuplist, name='CourierPickUpLists'),
]