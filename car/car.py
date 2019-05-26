from user.models import Product


class Cartitem():
    def __init__(self,book,amount):
        self.book = book
        self.amount = amount





class Cart():
    def __init__(self):
        self.save_price = 0
        self.total_price = 0
        self.cartitem = []
# 用来计算购物车中商品的节省金额 以及  总金额
    def sums(self):
        # print("进来了")
        self.save_price = 0
        self.total_price = 0
        for i in self.cartitem:
            self.total_price += int(i.book.dangdang_price) * i.amount
            self.save_price += (int(i.book.price) - int(i.book.dangdang_price)) * i.amount
    #  向购物车中添加 书籍的方法
    def add_book_toCart(self,bookid):
        # print("添加")
        if type(bookid) is int:
            bookid = bookid
        else:
            bookid = int(bookid)
        for i in self.cartitem:
            print(bookid,i.book.id,type(bookid),type(i.book.id))
            if bookid == i.book.id:
                print("增加数量")
                i.amount += 1
                self.sums()
                return None
        print(bookid,type(bookid))
        book = Product.objects.get(id = bookid)
        print("添加的书籍",book)
        self.cartitem.append(Cartitem(book,1))
        print("存在书记：",self.cartitem)
        self.sums()
    #  修改购物车中的商品数量
    def modify_book_cart(self,amount,bookid):
        self.book_price = 0
        for i in self.cartitem:
            if i.book.id == int(bookid):
                i.amount = amount
        self.sums()
    # 删除购物车
    def delete_book_cart(self,bookid):
        for i in self.cartitem:
            if i.book.id == int(bookid):
                self.cartitem.remove(i)
            self.sums()

    def clearcart(self):
        self.cartitem.clear()

