
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

    issue = order.objects.get(order_id=order_id)
    issue.status = "issue"
    issue.save()

    return render(request, 'IssueReport.html',{'issue': issue})

def storepage( request):
    return render_to_response('CourierStoreParcels.html')

@csrf_exempt
def storeinfo (request):
    if request.POST:
        parcels_trackid = request.POST.get("parcels_trackid")
        storeinfo = order.objects.get(track_id=parcels_trackid)
        return render(request, 'CourierStoreInfo.html', {'storeinfo': storeinfo})

def confirmparcel( request, order_id=None):

    confirmation = order.objects.get(order_id=order_id)
    confirmation.status = 'wait'
    confirmation.save()
    return render(request, 'ConfirmPage.html', {'confirmation': confirmation})
