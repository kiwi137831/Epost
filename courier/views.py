
from django.shortcuts import render, render_to_response, get_object_or_404

# Create your views here.
from django.http import HttpResponse


# def hello(request):
#     return HttpResponse("Hello world ! ")

def homepage(request):
    return render_to_response('CourierHomepage.html')

def pickuplist (request):

    # PickUpList = order.objects.filter(r_phone='0404').filter(status='wait')
    # return render(request, 'CourierPickuplists.html',{'pickuplist':PickUpList})
    return render(request, 'CourierPickuplists.html')