from django.conf.urls import url, include

from account import views
import account

urlpatterns = [

    url(r'^homepage/$', views.homepage, name='homepage'),
]