from django.conf.urls import url, include

from . import views

urlpatterns = [

    url(r'^homepage/$', views.homepage, name='homepage'),
url(r'^issuereport/$', views.issuereport, name='issuereport'),
url(r'^profile/$', views.profile, name='profile'),
url(r'^rate/$', views.rate, name='rate'),
url(r'^history/$', views.history, name='history')



]