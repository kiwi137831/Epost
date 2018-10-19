
from django.shortcuts import render, render_to_response, get_object_or_404
from account.models import *
from courier.models import order
from django.forms import fields
from django import forms
from django.views.decorators.csrf import csrf_exempt,csrf_protect
# Create your views here.
from django.http import HttpResponse


def homepage(request):
    return render_to_response('CourierHomepage.html')

def pickuplist (request):

    PickUpList = order.objects.filter(r_phone='0404').filter(status='wait')
    return render(request, 'CourierPickuplists.html', {'pickuplist': PickUpList})

def pickup( request, order_id=None):

    package = order.objects.get(order_id=order_id)
    package.status = 'Picked Up'
    package.save()

    return render(request, 'SuccessfulPage.html', {'package': package})

def issuereport( request, order_id=None):

    return render(request, 'IssueReport.html')

def storepage( request):
    return render_to_response('CourierStoreParcels.html')

@csrf_exempt
def storelist (request):
    if request.POST:
        receiver_phone = request.POST.get("receiver_phone")
        parcels_trackid = request.POST.get("parcels_trackid")
        print(receiver_phone)
        print(parcels_trackid)
        StoreList = order.objects.filter(r_phone="0404", track_id="1")
        return render(request, 'CourierStorelist.html', {'storelist': StoreList})
