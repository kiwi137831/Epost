from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms


def homepage(request):
    pass
    return render(request, 'login/homepage.html')

def index(request, user_id, career):
    USER = models.user.objects.get(user_id=user_id)
    Career = models.user.objects.get(career=career)
    return render(request, 'homepage.html',{'user': USER,'Career': Career})


def login(request):
    if request.session.get('is_login', None):
        return redirect('/homepage/')
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
                request.session['CAREER'] = user.career
                if user.career == 'customer':
                    return redirect(user.career + user.user_id + '/homepage/')
                else:
                    return redirect(user.career + user.user_id + '/homepage/')
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
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:
                message = 'The second time you enter your password is different！'
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.user.objects.filter(name=username)
                if same_name_user:
                    message = 'The username has already been registered.Please try again！'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.user.objects.filter(email=email)
                if same_email_user:
                    message = 'The email address has already been registered. Please use another email address！'
                    return render(request, 'login/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/homepage/')
    request.session.flush()
    return redirect('/homepage/')
