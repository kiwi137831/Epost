from django.conf.urls import url, include

from account import views
import account
from account.views import hello

urlpatterns = {
    url(r'homepage/$', views.homepage, name='homepage'),


}