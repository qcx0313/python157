# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    id = models.BigAutoField(primary_key=True)
    consignee = models.CharField(max_length=50, blank=True, null=True)
    detailaddress = models.CharField(max_length=100, blank=True, null=True)
    postalcode = models.CharField(max_length=10, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    mobilephone = models.CharField(max_length=20, blank=True, null=True)
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    extend = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Category(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    parent_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class ConfirmString(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user', blank=True, null=True)
    code = models.CharField(max_length=256, blank=True, null=True)
    code_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confirm_string'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Orderitem(models.Model):
    id = models.BigIntegerField(primary_key=True)
    productname = models.CharField(db_column='productName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(blank=True, null=True)
    amount = models.BigIntegerField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    orderid = models.ForeignKey('Orders', models.DO_NOTHING, db_column='orderid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orderitem'


class Orders(models.Model):
    id = models.BigIntegerField(primary_key=True)
    ordernumber = models.CharField(db_column='orderNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dateinproduct = models.DateTimeField(db_column='dateInProduct', blank=True, null=True)  # Field name made lowercase.
    freight = models.FloatField(blank=True, null=True)
    expenditure = models.FloatField(blank=True, null=True)
    address = models.ForeignKey(Address, models.DO_NOTHING, db_column='address', blank=True, null=True)
    customer = models.ForeignKey('User', models.DO_NOTHING, db_column='customer', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Product(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    face = models.CharField(max_length=100, blank=True, null=True)
    publishing_house = models.CharField(max_length=50, blank=True, null=True)
    edition = models.SmallIntegerField(blank=True, null=True)
    publishing_time = models.DateTimeField(blank=True, null=True)
    print_time = models.SmallIntegerField(blank=True, null=True)
    isbn = models.CharField(max_length=30, blank=True, null=True)
    word = models.CharField(max_length=20, blank=True, null=True)
    number_of_page = models.IntegerField(blank=True, null=True)
    format_of_book = models.CharField(max_length=20, blank=True, null=True)
    paper = models.CharField(max_length=20, blank=True, null=True)
    packagin = models.CharField(max_length=20, blank=True, null=True)
    emboitement = models.CharField(max_length=10, blank=True, null=True)
    sales = models.CharField(max_length=20, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    dangdang_price = models.FloatField(blank=True, null=True)
    review = models.BigIntegerField(blank=True, null=True)
    issue = models.DateTimeField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    sold_out = models.CharField(max_length=10, blank=True, null=True)
    recommand = models.CharField(max_length=10, blank=True, null=True)
    menus = models.ForeignKey(Category, models.DO_NOTHING, db_column='menus', blank=True, null=True)
    extend = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    extend = models.CharField(max_length=100, blank=True, null=True)
    c_time = models.DateTimeField(blank=True, null=True)
    has_confirm = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
