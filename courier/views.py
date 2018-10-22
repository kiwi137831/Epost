
from django.shortcuts import render, render_to_response, get_object_or_404
from account.models import *
from customer.models import order
from django.forms import fields
from django import forms
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from account.models import courier as Courier
# Create your views here.


from django.http import HttpResponse


def homepage(request, courier_id):
    courier = Courier.objects.get(courier_id=courier_id)

    return render(request,'CourierHomepage.html',{'courier':courier})

def cpickuplist (request,courier_id):
    courier = Courier.objects.get(courier_id=courier_id)
    PickUpList = order.objects.filter(company_id=courier.company_id).filter(status='wait pick up')

    return render(request, 'CourierPickuplists.html', {'pickuplist': PickUpList,'courier':courier})

def cpickup( request, courier_id=None,order_id=None):
    courier = Courier.objects.get(courier_id=courier_id)

    package = order.objects.get(order_id =order_id)


    package.status = 'Picked Up'
    package.save()

    return render(request, 'SuccessfulPagec.html', {'package': package})

def issuereport( request, order_id=None):

    issue = order.objects.get(order_id=order_id)
    issue.status = "issue"
    issue.save()

    return render(request, 'IssueReport.html',{'issue': issue})

def storepage( request, courier_id):



    courier = Courier.objects.get(courier_id=courier_id)

    return render(request, 'CourierStoreParcels.html', {'courier': courier,})


@csrf_exempt
def storeinfo (request,courier_id = None):
    courier = Courier.objects.get(courier_id=courier_id)

    if request.POST:
        parcels_trackid = request.POST.get("parcels_trackid")
        orderc= order.objects.get(track_id =parcels_trackid)

        storeinfo = order.objects.get(track_id=parcels_trackid)

        return render(request, 'CourierStoreInfo.html', {'storeinfo': storeinfo,'courier':courier,'order':orderc})

def confirmparcel( request, order_id=None,courier_id=None):


    confirmation = order.objects.get(order_id=order_id)
    confirmation.status = 'wait'
    confirmation.save()
    return render(request, 'ConfirmPage.html', {'confirmation': confirmation,'courier_id':courier_id,'order_id':order_id})
