import datetime
import random,string


from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import EmailMultiAlternatives

from django.shortcuts import render,HttpResponse,redirect,reverse
import hashlib
from regist.captcha.image import ImageCaptcha
from user import models
from user.models import User, ConfirmString
from django.core.mail import send_mail

def getCaptcha(request):
    image = ImageCaptcha()
    #生成随机码
    code = random.sample(string.ascii_letters+string.digits,4)
    code = ''.join(code)
    request.session['code']=code
    data = image.generate(code)
    return HttpResponse(data,'image/png')


# 登录页面，获取登录信息，判官是否注册，如果没有注册，请先进行注册，然后在进行登录。
def login(request):

    username = request.session.get("username")

    check = User.objects.filter(email=username)
    if check:
        total_price = request.session['cart'].total_price
        if total_price:
            region = User.objects.all()
            long_book = request.GET.get("long_book")
            return render(request, "indent.html", {"total_price": total_price,"username":username,"region":region,"long_book":long_book})
        reverse("user:index")
        return redirect("user:index")
    total_price = request.GET.get("total_price")
    print(total_price)
    if total_price:
        return render(request, "login.html", {"total_price": total_price})
    return render(request,"login.html")
def logout(request):
    request.session.flush()
    return render(request,"index.html")
def regist(request):
    return render(request,"register.html")

# 登录逻辑
def loginlogic(request):
    print(request.GET)
    code = request.POST.get("txtVerifyCode")
    code2 = request.session.get("code")
    if code.lower() == code2.lower():
        print('验证码正确',code2,code)
        username = request.POST.get("txtUsername")
        password = request.POST.get("txtPassword")
        print(username,password)
        print('mm',User.objects.get(email=username).password)
        password2 = check_password(password,User.objects.get(email=username).password)   #加密方式得到的是一串随机字符串,并且每次生成都不一样
        print(password2)
        check = User.objects.filter(email=username)
        print(check)
        if check and password2:

            request.session["username"]=username   #将登录状态存储在session
            request.session["password"]=password
            reverse("user:index")
            home = redirect("user:index")
            total_price = request.GET.get("total_price")
            print(total_price)
            if total_price:
                return render(request, 'indent.html',{"total_price":total_price,"username":username})

            if request.POST.get("remember"):    #点击记住我，存cookie,  cookie需要满的条件:用户名和密码输入正确+勾选记住我的选项
                home.set_cookie("username",username.encode('utf-8').decode('latin-1'), max_age=7 * 24 * 3600)
                home.set_cookie('password', password.encode('utf-8').decode('latin-1'), max_age=7 * 24 * 3600)
            return home

        else:
            return HttpResponse("登陆失败")
    else:
        return HttpResponse("验证失败")


def hash_code(name, now):
    h = hashlib.md5()
    name += now
    h.update(name.encode())
    return  h.hexdigest()

def make_confirm_string(new_user):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    code = hash_code(new_user.username,now)
    ConfirmString(code=code,code_time=now,user=new_user)
    return  code

def send_email(email,code):
    subject = 'python157'
    from_email = 'qcx313@sina.com'
    text_content = '欢迎访问www.baidu.com，祝贺你收到了我的邮件，有幸收到我的邮件说明你及其幸运'
    html_content = '<p>感谢注册<a href="http://{}/confirm/?code={}"target=blank>www.baidu.com</a>，\欢迎你来验证你的邮箱，验证结束你就可以登录了！</p>'.format('127.0.0.1',code)
    # 发送邮件所执行的方法以及所需的参数
    msg = EmailMultiAlternatives(subject, text_content,from_email, [email])
    # 发送的heml文本的内容
    msg.attach_alternative(html_content, "text/html")
    msg.send()

# 注册逻辑，获取email和密码，判断数据库中有没有密码，如果没有的话，利用事物进行添加,如果有的话，从新注册
def registlogic(request):
    code1 = request.POST.get("txt_vcode")   #获取验证码
    code2 = request.session.get("code")
    if code1.lower() == code2.lower():
        email = request.POST.get("txt_email")
        username = request.POST.get("txt_username")
        password = request.POST.get("txt_password")
        password = make_password(password,None,'default')
        new_user = models.User.objects.create(email=email,username=username, password=password)
        code = make_confirm_string(new_user)
        send_email(email,code)
        reverse("regist:login")
        res = User.objects.filter(email=email)  # 查询数据库中是否有email
        if res:
            return HttpResponse('用户名已存在，请重新输入')
        return redirect("regist:login")  # 注册完成界面，完成注册后，跳入登录界面
    else:

        return HttpResponse("注册错误")



# 用Ajax 判断用户名是否存在
def checkcode(request):
    code = request.POST.get("code")  # 输入框中输入的验证码
    code2 = request.session.get('code')  # 获取session的随机验证码
    if  code.lower() == code2.lower():
        return HttpResponse("验证码正确")
    else:
        return HttpResponse("验证码错误")

# 用Ajax 判断用户名是否存在
def checkusername(request):
    name = request.POST.get("name")   #获取文本框中的name
    user = User.objects.filter(email=name)
    if user:
        return HttpResponse("用户名已存在")
    else:
        return HttpResponse("用户名合法")



