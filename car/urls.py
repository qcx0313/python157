
from django.urls import path
from car import views

app_name = "car"

urlpatterns = [
    path("cart/",views.cart,name="cart"),
    path("add_cart/",views.add_cart,name="add_cart"),
    path("change_cart/",views.change_cart,name="change_cart"),
    path("delete_cart/",views.delete_cart,name="delete_cart"),

    path("indent/",views.indent,name="indent"),
    path("indentok/",views.indentok,name="indentok"),
    path("indetlogin/",views.indetlogin,name="indetlogin"),

    path('address_name/',views.address_name,name ='address_name'),
    path('addr/',views.addr,name ='addr'),
    path('code/',views.code,name='code'),
    path('phone/',views.phone,name='phone'),
    path('settle/',views.settle,name ='settle'),

    path("registerok/",views.registerok,name="registerok"),
    path("register_email/",views.register_email,name="register_email"),

]