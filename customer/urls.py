from django.conf.urls import url, include

from customer import views
import customer

urlpatterns = [

    url(r'^CourierHomepage/$', views.homepage, name='CourierHomepage'),

]