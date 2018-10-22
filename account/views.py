from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms
from django.db.models import Max

def index(request):
    pass
    return render(request, 'login/homepage.html')

def homepage(request, user_id):
    USER = models.user.objects.get(user_id=user_id)
    return render(request, 'homepage.html',{'USER', USER})

def login(request):
    if request.session.get('is_login', None):
        return redirect('/homepage/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = 'you should fill in all content'
        if login_form.is_valid():
            account = login_form.cleaned_data.get('account')
            #name = login_form.cleaned_data.get('name')
            password = login_form.cleaned_data.get('password')
            user_id = login_form.cleaned_data.get('user_id')
            # ....
            try:
                user = models.user.objects.get(account=account)
            except:
                message = 'User does not exist!'
                return render(request, 'login/login.html', locals())

            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.user_id
                request.session['user_name'] = user.name
                if user.type == 'customer':
                    return redirect('/customer/' + user.user_id + '/homepage/')
                else:
                    return redirect('/courier/' + user.user_id + '/homepage/')
            else:
                message = 'wrong password'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect('/homepage/')

    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        message = 'check the information!'
        if register_form.is_valid():
            account = register_form.cleaned_data['account']
            name = register_form.cleaned_data['name']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            phone = register_form.cleaned_data['phone']
            address = register_form.cleaned_data['address']
            gender = register_form.cleaned_data['gender']
            age = register_form.cleaned_data['age']
            type = register_form.cleaned_data['type']
            if password1 != password2:
                message = 'The second time you enter your password is different！'
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.user.objects.filter(account=account)
                if same_name_user:
                    message = 'The account has already been registered.Please try again！'
                    return render(request, 'login/register.html', locals())

                userid = models.user.objects.all().aggregate(Max('user_id'))
                userid= str(int(userid['user_id__max'])+1)

                models.user.objects.create(user_id=userid,account=account, name=name,
                                           password=password1, email=email,
                                           phone=phone, gender=gender,
                                           address=address,
                                           age=age, type=type)


                return redirect('/login/')  # 自动跳转到登录页面
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/homepage/')
    request.session.flush()
    return redirect('/homepage/')
