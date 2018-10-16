
from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms
from face_recognition


import hashlib


def hash_code(s, salt='epost'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()

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

            if user.password == hash_code(password):
                request.session['is_login'] = True
                request.session['user_id'] = user.id
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
        return redirect('/index/')
    request.session.flush()
    return redirect('/index/')

def loginFaceCheck(request):

    ## 人脸登陆验证

    if request.method == "POST" and request.is_ajax():
        # 获取base64格式的图片
        faceImage = request.POST.get('faceImg')
        # 提取出base64格式，并进行转换为图片
        index = faceImage.find('base64,')
        base64Str = faceImage[index+6:]
        img = base64.b64decode(base64Str)
        # 将文件保存
        backupDate = time.strftime("%Y%m%d_%H%M%S")
        if int(request.POST.get('id')) == 0 :
            fileName = BASE_LOGIN_LEFT_PATH +"LeftImg_%s.jpg" % (backupDate)
        else:
            fileName = BASE_LOGIN_RIGHT_PATH + "RightImg_%s.jpg" % (backupDate)
        file = open(fileName, 'wb')
        file.write(img)
        file.close()
        # 删除多余的图片
        filesLeft = os.listdir(BASE_LOGIN_LEFT_PATH)
        filesLeft.sort()
        leftImgCount = filesLeft.__len__()
        filesRight = os.listdir(BASE_LOGIN_RIGHT_PATH)
        filesRight.sort()
        RightImgCount = filesRight.__len__()

        if leftImgCount > 100:
            # 图片超过100个，删除一个
            os.unlink(BASE_LOGIN_LEFT_PATH +filesLeft[0])
        if RightImgCount > 100:
            # 图片超过100个，删除一个
            os.unlink(BASE_LOGIN_RIGHT_PATH + filesRight[0])

        # 对图片进行人脸识别比对
        canLogin = False
        AuthName = "未授权用户"

        # 1> 加载相机刚拍摄的人脸
        unknown_face = face_recognition.load_image_file(fileName)
        unknown_face_tmp_encoding = []
        try:
            unknown_face_tmp_encoding = face_recognition.face_encodings(unknown_face)[0]
        except IndexError:
            canLogin = False  # 图片中未发现人脸

        # 2> 进行比对

        ### 第一种方法
        # results = face_recognition.face_distance(known_face,unknown_face_tmp_encoding)
        # 小于0.6即对比成功。但是效果不好，因此我们设置阈值为0.4,
        # for i, face_distance in enumerate(results):
        #     if face_distance <= 0.4:
        #         canLogin = True
        #         AuthName = os.listdir(BASE_LOGIN_AUTH_PATH)[i][:-4]

        ### 第二中方法
        results1 = face_recognition.compare_faces(known_face,unknown_face_tmp_encoding,0.4)
        for i, face_distance in enumerate(results1):
            if face_distance == True:
                canLogin = True
                AuthName = os.listdir(BASE_LOGIN_AUTH_PATH)[i][:-4]

        JsonBackInfo = {
            "canLogin": canLogin,
            "AuthName": AuthName
        }

        return JsonResponse(JsonBackInfo)




