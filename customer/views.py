from django.shortcuts import render
from django.db.models import Max
from django.shortcuts import render, render_to_response, get_object_or_404,redirect

# Create your views here.
from account.models import user as User
from account.models import notice as noticeboard
from customer.models import order
from courier.models import company
from .forms import IssueForm, OrderForm
def homepage(request,user_id):
    user = User.objects.get(user_id=int(user_id))
    return render(request,'homepage.html',{'user': user})




def pickuplist (request, user_id):

    user = User.objects.get(user_id = int(user_id))
    PickUpList = order.objects.filter(r_phone= user.phone).filter(status='wait')


    return render(request, 'PickUpList.html',{'pickuplist':PickUpList,'user':user})



def pickup( request, user_id,order_id=None):
    user = User.objects.get(user_id=int(user_id))
    package = order.objects.get(order_id=order_id)
    package.status = 'Picked Up'
    package.save()

    return render(request, 'SuccessfulPage.html', {'package': package,'user':user})



def issuereport( request, order_id=None, user_id = None):
    if request.method == "POST":
        issueform = IssueForm(request.POST)
        if issueform.is_valid():  # 所有验证都通过
            # do something处理业务

            instance = issueform.save(commit=False)
            # 保存该实例
            issueform.save()

            return redirect('http://127.0.0.1:8000/customer/1/homepage/')

    else:

        issueform = IssueForm(initial={'order_id':order_id,'title':'','content':'','user_id':user_id})

    user = User.objects.get(user_id=int(user_id))

    return render(request, 'IssueReport.html',{'user': user,'order_id':order_id,'issueform':issueform})


def notice( request, order_id=None, user_id = None):

    notice = noticeboard.objects.all()
    user = User.objects.get(user_id=user_id)

    return render(request, 'NoticeBoard.html',{'noticeboard': notice,'user':user})



# create new  order

def send( request, user_id = None):
    user = User.objects.get(user_id=int(user_id))
    if request.method == "POST":
        orderform = OrderForm(request.POST)
        if orderform.is_valid():  # 所有验证都通过
            # do something处理业务

            orderid = order.objects.all().aggregate(Max('order_id'))

            # get model of order
            # get the id name of company
            companyid=orderform.cleaned_data.get("company_id")
            ordercompany=company.objects.get(company_id=companyid)

            order_d= orderid['order_id__max']
            order_id= str(int(order_d)+1)
            #track_id=ordercompany.name+order_id

            receiver= orderform.cleaned_data.get("receiver")
            r_address = orderform.cleaned_data.get("receiver_address")
            r_postcode = orderform.cleaned_data.get("r_postcode")
            r_phone = orderform.cleaned_data.get("receiver_phone")

            sender = orderform.cleaned_data.get("sender")
            s_address = orderform.cleaned_data.get("sender_address")
            s_postcode = orderform.cleaned_data.get("s_postcode")
            s_phone = orderform.cleaned_data.get("sender_phone")
            weight = orderform.cleaned_data.get("weight")
            company_id = orderform.cleaned_data.get("company_id")
            price = str(int(ordercompany.price) * int(weight))
            status = 'wait pick up'




            # 保存该实例

            order.objects.create(order_id=order_id,status=status,price=price,r_address=r_address,r_phone=r_phone,r_postcode=r_postcode,receiver=receiver,s_address=s_address,s_phone=s_phone,s_postcode=s_postcode,sender=sender,weight=weight,company_id=company_id)

            track_id = ordercompany.name + order_id
            order.objects.filter(order_id= order_id).update(track_id=track_id)

            return render(request, 'Payment.html', {'price': price,'track_id':track_id,'user':user})

    else:


        orderform = OrderForm

    user = User.objects.get(user_id=int(user_id))

    return render(request, 'OrderPage.html', {'user': user, 'orderform': orderform})

