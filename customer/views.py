from __future__ import  unicode_literals

from django.utils import timezone
from django.shortcuts import render, render_to_response
from customer import models
from account.models import user

# Create your views here.

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
        password = request.POST.get("password", None)
        name = request.POST.get("name", None)
        email = request.POST.get("email", None)
        phone = request.POST.get("phone", None)
        address = request.POST.get("address", None)
        gender = request.POST.get("gender", None)
        age = request.POST.get("age", None)
            # 设置 order_id = 1
        user = models.user.objects.create(
            user_id='1',
            account='1',
            password=password,
            name=name,
            type='1',
            email=email,
            phone = phone,
            address = address,
            gender = gender,
            age = age)
        user.save()
        return render(request, "profile.html")
        # 显示存了什么
    return render(request, "profile.html")

def rate(request):
    if request.method == "POST":
        level = request.POST.get("level", None)
        ratecontent = request.POST.get("content", None)
            # 设置 order_id = 1
        user = models.user.objects.create(
            rate_id='1',
            date=timezone.now(),
            level=level,
            content=ratecontent,
            order_id='1',
            writer_id='1',
            delivery_id = '1',)
        user.save()
        return render(request, "profile.html")
        # 显示存了什么
    return render(request, "profile.html")

