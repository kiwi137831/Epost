
from django.urls import path
from account import views
from django.conf.urls import url


urlpatterns = [
    # post views
    path('<str:career>/<str:user_id>/homepage/', views.index, name='index'),
]