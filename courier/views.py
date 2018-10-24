
from django.shortcuts import render, render_to_response, get_object_or_404,redirect
from account.models import *
from customer.models import order
from django.forms import fields
from django import forms
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from account.models import courier as Courier
from account.models import notice as noticeboard
from courier.models import issue as Issue
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

def issue( request, courier_id=None,order_id=None):

    courier = Courier.objects.get(courier_id=courier_id)

    return render(request, 'IssueReport.html', {'courier': courier,'order':order})
@csrf_exempt
def issuereport( request, order_id=None, courier_id = None):
        courier = Courier.objects.get(courier_id=courier_id)

        if request.POST:
            issue_title= request.POST.get("issue_title")
            issue_content= request.POST.get("issue_content")
            issuepackage = Issue(order_id=order_id,title=issue_title,content= issue_content)

            issuepackage.save()

            return redirect('http://127.0.0.1:8000/courier/1/CourierHomepage/')

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

def couriernotice( request, order_id=None,courier_id = None):

    notice = noticeboard.objects.all()
    courier = Courier.objects.get(courier_id=courier_id)

    return render(request, 'CourierNoticeBoard.html',{'noticeboard': notice,'courier':courier})
