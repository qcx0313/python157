from django.urls import path
from regist import views

app_name = "regist"

urlpatterns = [
    path("getCaptcha/", views.getCaptcha, name="getCaptcha"),
    path("regist/",views.regist,name="regist"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    path("regist/",views.regist,name="regist"),
    path("registlogic/",views.registlogic,name="registlogic"),
    path("loginlogic/",views.loginlogic,name="loginlogic"),
    path("checkcode/",views.checkcode,name="checkcode"),
    path("checkusername/",views.checkusername,name="checkusername"),
]


