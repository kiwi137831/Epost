from __future__ import  unicode_literals

from django.utils import timezone
from django.shortcuts import render, render_to_response

import account
import customer


# Create your views here.
from customer.models import order


def homepage(request):
    return render_to_response('homepage.html')

#页尾加个success  notice，url读取id没做
def issuereport(request):
    if request.method == "POST":
        contentinput = request.POST.get("issuescontent", None)
    #设置 order_id = 1
        issuesInput = models.issues.objects.create(
        order_id='1',
        title = '1',
        content = contentinput,
        date = timezone.now(),
        writer_id = '1',
        status = '1')
        issuesInput.save()
        return render(request, "issuereport.html")
    #显示存了什么
    return render(request, "issuereport.html")


    # issuesA = issues.objects.all()
    # content = {'issuesB':issuesA}
#profile  这个页面  应该是 表单显示信息，然后可更改，先做成插入的样子，后续再改
def profile(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id", None)
        password = request.POST.get("password", None)
        name = request.POST.get("name", None)
        email = request.POST.get("email", None)
        phone = request.POST.get("phone", None)
        address = request.POST.get("address", None)
        gender = request.POST.get("gender", None)
        age = request.POST.get("age", None)
            # 设置 order_id = 1
        user = account.models.user.objects.get(user_id=user_id)
        user.user_id='1'
        user.account='1'
        user.password=password
        user.name=name
        user.type='1'
        user.email=email
        user.phone = phone
        user.address = address
        user.gender = gender
        user.age = age
        #这种save操作就相当于在update
        user.save()
        return render(request, "profile.html")
        # 显示存了什么   这里应该是依据id查找，不是select all
    user = account.models.user.objects.get(user_id="1")
    return render(request, "profile.html", {"user":user})

def rate(request):
    if request.method == "POST":
        level = request.POST.get("level", None)
        ratecontent = request.POST.get("ratecontent", None)
            # 设置 order_id = 1
        user = customer.models.rate.objects.create(
            rate_id='1',
            date=timezone.now(),
            level=level,
            content=ratecontent,
            order_id='1',
            writer_id='1',
            delivery_id = '1',)
        user.save()
        return render(request, "rate.html")
        # 显示存了什么
    return render(request, "rate.html")


def history(request):
    if request.method == "POST":
        delete_all = request.POST.get("delete_all", None)
        if delete_all == "Delete All":
            s_phone = request.POST.get("s_phone", None)
            customer.models.order.objects.filter(s_phone = s_phone).delete()
            return render(request, "history.html")
        else:
            order_id = request.POST.get("order_id", None)
        #应该加个status检查
            customer.models.order.objects.filter(order_id=order_id).delete()
            return render(request, "history.html")
        # 显示存了什么   这里应该是依据id查找，不是select all   order里缺少user_id
    orders = customer.models.order.objects.all()
    return render(request, "history.html", {"orders":orders})

