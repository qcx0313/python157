
from django.urls import path
from user import views

app_name = "user"

urlpatterns = [
    path("index/",views.index,name="index"),
    path("books/",views.books,name="books"),
    path("booklist/",views.booklist,name="booklist"),
    path("del_login/",views.del_login,name="del_login"),

    # path("home/",views.home,name="home"),

]