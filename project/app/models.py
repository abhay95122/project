from audioop import add
from operator import index
from re import M
from statistics import mode
from unicodedata import name
from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Menu(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Permission(models.Model):
    act_name = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    menu_id = models.ForeignKey(Menu)

class Rolepermission(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role_id = models.ForeignKey(Role)
    permission_id = models.ForeignKey(Permission)


class Department(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(models.Model):
    emp_user_id = models.IntegerField(unique=True, null=True)
    name = models.CharField(max_length=150,null=False)
    email = models.EmailField(max_length=255,null=False)
    password = models.CharField(max_length=80)
    mobile_number = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    joining_date = models.DateField(null=False)
    leave_date = models.DateField(null=True)
    status = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    department_id = models.ForeignKey(Department)
    role = models.ForeignKey(Role)
    class Meta():
       indexes = [
            models.Index(fields=['name',]),
        ]

class Vender(models.Model):
    vender_name = models.CharField(max_length=50)
    vender_mobile_number = models.CharField(max_length=12)
    vender_email = models.EmailField(max_length=250)
    vender_address = models.CharField(max_length=100)   
    PAN_number = models.CharField(max_length=10)
    GST_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
       indexes = [
            models.Index(fields=['-vender_name',]),
        ]


class MasterProduct(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MasterVariant(models.Model):
    variant_name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
    product_img = models.ImageField()
    pro_id = models.IntegerField()
    Tag_Number = models.CharField(max_length=30)
    purchase_price = models.IntegerField()
    assign_product = models.IntegerField()
    product_status = models.CharField(max_length=10)
    description = models.TextField()
    status = models.SmallIntegerField()
    buy_date = models.DateTimeField(auto_now_add=True)
    to_date = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    masterproduct_id = models.ForeignKey(MasterProduct)
    mastervariant_id = models.ForeignKey(MasterVariant)# json


class InStockProduct(models.Model):
    from_date = models.DateTimeField(auto_now_add=True)
    to_date = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product_id = models.ForeignKey(Product)
    class Meta:
       indexes = [
            models.Index(fields=['-from_date',]),
            models.Index(fields=['-to_date']),
        ]

class AssignProduct(models.Model):
    from_date = models.DateTimeField(auto_now_add=True)
    to_date = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product_id = models.ForeignKey(Product)
    user_id = models.ForeignKey(User)
    class Meta:
       indexes = [
            models.Index(fields=['-from_date',]),
            models.Index(fields=['-to_date']),
        ]
    
class ToBeRepairProduct(models.Model):
    from_date = models.DateTimeField(auto_now_add=True)
    to_date = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField()
    product_id = models.ForeignKey(Product)
    class Meta:
       indexes = [
            models.Index(fields=['-from_date',]),
            models.Index(fields=['-to_date']),
        ]

class ServiceProduct(models.Model):
    from_date = models.DateTimeField(auto_now_add=True)
    to_date = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product_id = models.ForeignKey(Product)
    expense = models.IntegerField()
    vender_id = models.ForeignKey(Vender)
    class Meta:
       indexes = [
            models.Index(fields=['-from_date',]),
            models.Index(fields=['-to_date']),
        ]
    
class SaleProduct(models.Model):
    from_date = models.DateTimeField(auto_now_add=True)
    to_date = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    amout = models.IntegerField()
    product_id = models.ForeignKey(Product)
    vender_id = models.ForeignKey(Vender)
    class Meta:
       indexes = [
            models.Index(fields=['-from_date',]),
            models.Index(fields=['-to_date']),
        ]

class ScrapLostProduct(models.Model):
    date = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    amout = models.IntegerField()
    description = models.CharField(max_lengt=100)
    type = models.CharField(max_length=10)
    user_id = models.ForeignKey(User)
    product_id = models.ForeignKey(Product)
    class Meta:
       indexes = [
            models.Index(fields=['-date',]),
        ]

class AssignProductToProduct(models.Model):
    assign_product_id = models.IntegerField()
    product_id = models.IntegerField()
    from_date = models.DateTimeField(auto_now_add=True)
    to_date = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
       indexes = [
            models.Index(fields=['-from_date',]),
            models.Index(fields=['-to_date']),
        ]



class Fine(models.Model):
    amout = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    description = models.CharField(max_lengt=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User)
    product_id = models.ForeignKey(Product)

class Request(models.Model):
    date = models.DateTimeField(auto_now=True)
    description = models.CharField(max_lengt=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField()
    user_id = models.ForeignKey(User)
    product_id = models.ForeignKey(Product)




