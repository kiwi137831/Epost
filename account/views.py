
from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms


def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login', None):
        return redirect('/index/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = 'you should fill in all content'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            # ....
            try:
                user = models.user.objects.get(name=username)
            except:
                message = 'User does not exist!'
                return render(request, 'login/login.html', locals())

            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.user_id
                request.session['user_name'] = user.name
                return redirect('/index/')
            else:
                message = 'wrong password'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        message = 'check the information!'
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            phone = register_form.cleaned_data['phone']
            address = register_form.cleaned_data['address']
            career = register_form.cleaned_data['career']
            age = register_form.cleaned_data['age']
            if password1 != password2:
                message = 'The second time you enter your password is different！'
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.user.objects.filter(name=username)
                if same_name_user:
                    message = 'The username has already been registered.Please try again！'
                    return render(request, 'login/register.html', locals())

                new_user = models.user.objects.create()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.phone = phone
                new_user.address = address
                new_user.age = age
                new_user.career = career
                new_user.save()
                return redirect('/login/')
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/index/')
    request.session.flush()
    del request.session['is_login']
    del request.session['user_id']
    del request.session['user_name']
    return redirect('/index/')




