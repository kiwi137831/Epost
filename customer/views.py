from django.shortcuts import render
from django.shortcuts import render, render_to_response, get_object_or_404
# Create your views here.
from account.models import *
from customer.models import order
def homepage(request):
    return render_to_response('homepage.html')




def pickuplist (request):

    PickUpList = order.objects.filter(r_phone='0404').filter(status='wait')


    return render(request, 'PickUpList.html',{'pickuplist':PickUpList})



def pickup( request, order_id=None):

    package = order.objects.get(order_id=order_id)
    package.status = 'Picked Up'
    package.save()

    return render(request, 'SuccessfulPage.html', {'package': package})



def issuereport( request, order_id=None):



    return render(request, 'IssueReport.html')



def pickddddup(request):
    q_list = Question.published.all()

    paginator = Paginator(q_list, 4)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'subject.html', {'questions': questions})