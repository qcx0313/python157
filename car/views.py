import random

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from car.car import Cart
from user import models
from user.models import Product, Orderitem, Orders
from user.models import Address


def cart(request):
    cart = request.session.get("cart")  #从session中获取购物车  购物车对象 list total_price save_price
    if cart:
        total_price = cart.total_price
        save_price = cart.save_price
        cart = cart.cartitem

        long_book = len(cart)
        print(long_book)
        return render(request, "car.html",
                      {"cart": cart, "total_price": total_price, "save_price": save_price, "lang_book": long_book})
    return render(request, "car.html")


# def cart(request):
#     cart = request.session.get("cart")
#     # delete_cart = request.session.get("delete_cart")
#     # cart.clearcart()
#
#     username = request.session.get("username")
#     if cart:
#         total_price = cart.total_price
#         save_price = cart.save_price
#         cart = cart.cartitem
#         # if delete_cart:
#         #     delete_cart = delete_cart.cartitem
#         long_book = len(cart)
#         print(long_book)
#         return render(request, "cart/car.html", {"cart": cart, "total_price": total_price, "save_price": save_price,"lang_book":long_book,"username":username})
#     return render(request,"cart/car.html",{"username":username})

# 添加购物车
def add_cart(request):
    bookid = request.POST.get("bookid")
    cart = request.session.get("cart")  #将购物车存储到session中
    if request.GET.get("bookid"):
        bookid = request.GET.get("bookid")
    # 判断购物车是否存在
    if not cart:  #判断购物车是否为空,如果购物车为空,调用增加书籍的方法，然后将购物车存入session中
        cart = Cart()
        cart.add_book_toCart(bookid)   #cart购物车已经存在，调用增加书籍的方法
    else:
        print(bookid, type(bookid))
        cart.add_book_toCart(bookid)
    request.session["cart"] = cart    #将购物车存入session中
    print(cart)
    return HttpResponse("添加成功")

#修改购物车
def change_cart(request):
    print("我进来了")
    bookid = int(request.POST.get("bookid"))  #获取书的id
    cart = request.session.get("cart")        #从session中获取购物车
    amount = int(request.POST.get("amount"))  #获取书的数量
    cart.modify_book_cart(amount, bookid)    #调用购物车的修改的方法
    request.session["cart"] = cart          #将购物车重新存入session中
    print(amount)
    dangdang_price = Product.objects.filter(pk=bookid)[0].dangdang_price  #从Product中找出每本书的dangdang_price
    print(dangdang_price)
    dangdang_price = int(dangdang_price) * int(amount)   #计算总的dangdang_price的价格
    total_price = cart.total_price
    save_price = cart.save_price
    print('sdfgojaseprkthjeroikng', total_price, save_price)
    monery = {"total_price": total_price, "save_price": save_price, "dangdang_price": dangdang_price}
    print(monery)
    return JsonResponse(monery)

# 删除购物车
def delete_cart(request):
    bookid = request.POST.get("bookid")  #获取书的id
    cart = request.session.get("cart")   #从session中获取购物车
    cart.delete_book_cart(bookid)        #调用删除的方法
    request.session["cart"] = cart           #将购物车重新存入session中
    total_price = cart.total_price
    save_price = cart.save_price
    monery = {"total_price": total_price, "save_price": save_price}
    return JsonResponse(monery)

#收货地址界面
def indent(request):
    cart = request.session.get("cart")
    for i in cart.cartitem:
        print(i.book.name)
    print(type(cart.cartitem[0]), type(cart.cartitem))

    total_price = cart.total_price

    cart = cart.cartitem

    return render(request, 'indent.html', {"cart": cart,'total_price':total_price,})


    # def indentok(request):
#     return render(request, 'indent ok.html')


def indetlogin(request):
    address_name = request.POST.get('name')
    print(address_name)
    addr = request.POST.get('addr')
    code = request.POST.get('code')
    phone_name = request.POST.get('phone')
    cart = request.session.get("cart")
    c = Address(consignee=address_name, detailaddress=addr, postalcode=code, telephone=phone_name)
    c.save()
    print(1111111)
    # for i in cart.cartlen:
    #     oic =Orderitem.objects.filter(orderid=1)[0]
    #     orderid =oic.orderid
    #     oi =Orderitem(productname=i.book.name,price=i.total_price,orderid=orderid)
    #     oi.save()
    # l ='1234567890'
    # ord_num=''.join(random.sample(1,9))
    # order =Orders(ordernumber=ord_num,expenditure=cart.total_price)
    # order.save()
    # order_id =order.id
    # request.session['order_id']=order_id
    return redirect('car:indentok')


def indentok(request):
    cart = request.session.get("cart")
    print(cart.cartitem[0])
    return render(request, 'indent ok.html', {"cart": cart, })


# 点击结算按钮
def settle(request):
    login_status =request.session.get('login_status')
    if login_status=='ok':
        cart =request.session.get('cart')
        return render(request,'indent.html',{'cart':cart})
    else:
        request.session['login_status']=login_status
        return render(request,'login.html')




# 利用Ajax服务器接受请求
# 收货人
def address_name(request):
    address_name = request.POST.get('address_name')
    print('address_name=', address_name)
    # con =Address.objects.filter(consignee=address_name)
    if not address_name:
        return HttpResponse('不合法')
    else:

        return HttpResponse('合法')


# 地址
def addr(request):
    addr = request.POST.get('addr')
    print('addr=', addr)
    if not addr:
        return HttpResponse('不合法')
    else:

        return HttpResponse('合法')


# 编码
def code(request):
    code = request.POST.get('code')
    print('code=', code)
    if len(code) == 6 and code.isdigit():
        return HttpResponse('合法')
    else:

        return HttpResponse('不合法')


# 电话格式
def phone(request):
    phone_name = request.POST.get('phone')
    print('phone_name=', phone_name)
    if len(phone_name) == 11 and (phone_name)[0] == '1' and phone_name.isdigit():
        return HttpResponse('合法')
    else:
        return HttpResponse('不合法')


# 点击结算按钮
def settle(request):
    login_status = request.session.get('login_status')
    if login_status == 'ok':
        cart = request.session.get('cart')
        return render(request, 'indent.html', {'cart': cart})
    else:
        request.session['login_status'] = login_status
        return render(request, 'login.html')


def registerok(request):
    return render(request, 'register ok.html')


def register_email(request):
    return render(request, 'register_email_check .html')
