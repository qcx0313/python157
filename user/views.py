from django.core.paginator import Paginator
from django.shortcuts import render, redirect

# Create your views here.
from user.models import Category, Product

# 渲染主页面
def index(request):
    cate = Category.objects.all() #从分类表中获取目录的信息
    books = Product.objects.all()   #从数据库中获取书的信息     主编推荐-----新书上架
    pagtor = Paginator(books, per_page=8)   #实现分页，每页有8本书的信息
    page1 = pagtor.page(1)
    page2 = pagtor.page(2)

    return render(request, 'index.html',{'cate':cate,'page1':page1,'page2':page2,'books':books})

# 书的详细信息
def books(request):
    ids = request.GET.get('ids')  #获取页面拼接的id
    book = Product.objects.get(id=ids)
    # book = Product.objects.filter(pk=id)
    monery = round(float(book.dangdang_price) / float(book.price) * 10.0,2) #打折
    print(book)
    return render(request, 'Book details.html', {'book':book,'monery':monery})

    # id = request.GET.get("id")
    # book = Product.objects.filter(pk=id)[0]
    # monery = float(book.dangdang_price) / float(book.price) * 10.0
    # second_cate_id = book.second_cate_id
    # two = TCategory.objects.filter(pk=second_cate_id)[0]
    # one = CategoryDirectory.objects.filter(pk=two.parent_id)[0]
    # return render(request, "Book details.html", {"book": book, "monery": monery, "one": one, "two": two})

def booklist(request):
    pnging = request.GET.get('pnging')
    iids = request.GET.get('ids')
    iidd = request.GET.get('ids')
    book = Product.objects.get(id=iidd)
    iids = Category.objects.filter(parent_id=iids) #获取一级目录
    content = list()
    for i in iids:
        content += list(Product.objects.filter(menus=i.id))
    books = Category.objects.all()
    number = request.GET.get('page')   #获取页码数
    book = Product.objects.all()
    book_id = Product.objects.all()
    pagtor = Paginator(content, per_page=4)   # 构造分页器对象
    print('123123')
    if pnging:
        number = pnging
    if number:
        number = int(number)
    if number is None:    #如果没有页码，默认为第一页
        number = 1
    page = pagtor.page(number)   #获取第number页
    return render(request, 'booklist.html', locals())

def del_login(request):
    del request.session['username']  # 清除session
    return redirect('user:index')  # 重定向到主页


    # cate = Category.objects.all()
    # books = Product.objects.all()
    # pagtor = Paginator(books, per_page=6)
    # page1 = pagtor.page(1)
    # page2 = pagtor.page(2)
    #
    # return render(request, 'booklist.html', {'cate': cate, 'page1': page1, 'page2': page2, 'books': books})

    # category_id = request.GET.get("category_id")
    # directory_id = request.GET.get("directory_id")
    # cd_name = request.GET.get("cd_name")
    # if cd_name:
    #     directory_id = Category.objects.filter(directory_name=cd_name)[0].id
    # #
    # if category_id:
    #     book = Product.objects.filter(second_cate_id=category_id)
    #     category_name = Category.objects.filter(pk=category_id)[0].name
    #     directory_id = Category.objects.filter(pk=category_id)[0].parent_id
    #     number = request.GET.get('num')
    #     if not request.GET.get('num'):
    #         number = 1
    #     if request.GET.get("turn"):
    #         number = request.GET.get("turn").value
    #     pagtor = Paginator(book, per_page=6)
    #     page = pagtor.page(number)
    #     book = list(book)
    #     if len(book) % 6 == 0:
    #         count = len(book) // 6
    #     else:
    #         count = len(book) // 6 + 1
    #     count_book = len(book)
    #     return render(request, "booklist.html",{"cate":cate,"books":books,"category_id": category_id, "directory": directory_id,"page": page,"category_name": category_name, "count": count,"count_book": count_book})
    # if directory_id:
    #     book = Category.objects.filter(parent_id=directory_id)
    #     directory_name = Category.objects.filter(pk=directory_id)[0].directory_name
    #     book = list(book)
    #     l = []
    #     for i in book:
    #         l.append(i.id)
    #     book_r = Product.objects.filter(second_cate_id__in=l)
    #     number = request.GET.get('num')
    #     if not request.GET.get('num'):
    #         number = 1
    #     if request.GET.get("turn"):
    #         number = request.GET.get("turn").value
    #     pagtor = Paginator(book_r, per_page=6)
    #     page = pagtor.page(number)
    #     book_r = list(book_r)
    #     if len(book) % 6 == 0:
    #         count = len(book_r) // 6
    #     else:
    #         count = len(book_r) // 6 + 1
    #     count_book = len(book_r)
    #     return render(request, "booklist.html",{"cate":cate,"books":books,"directory_id": directory_id,"page": page,"directory_name": directory_name,"count": count,"count_book": count_book})
    # return render(request, 'booklist.html', {'cate': cate, 'page1': page1, 'page2': page2, 'books': books,"category_id": category_id, "directory": directory_id,"page": page,"category_name": category_name, "count": count,"count_book": count_book,'directory_name':directory_name})



