from django.db import models

# Create your models here.

class userregister(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    number=models.IntegerField(default=0)
    address=models.TextField()
    password=models.CharField(max_length=12)

    # def __str__(self):
    #     return (self.name)+" "+str(self.email)

class Category(models.Model):
    categoryname=models.CharField(max_length=200)
    image=models.ImageField(upload_to='category_img',blank=True)
    def __str__(self):
        return (self.categoryname)

class product (models.Model):
    name = models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    discription=models.TextField()
    image=models.ImageField(upload_to='product_img')
    price=models.IntegerField()
    quantity=models.IntegerField()
    vendorid=models.CharField(max_length=200,default="")

class contactus(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    number = models.IntegerField()
    address = models.CharField(max_length=250)
    comment = models.CharField(max_length=500)

class Vendorregister(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    number=models.IntegerField()
    address=models.TextField()
    password=models.CharField(max_length=12)

class cart(models.Model):
    userid=models.CharField(max_length=200)
    productid=models.CharField(max_length=200)
    vendorid=models.CharField(max_length=200)
    orderid=models.CharField(max_length=200)
    quantity=models.CharField(max_length=200)
    totalprice=models.CharField(max_length=200)

class Order(models.Model):
    userid=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    email=models.EmailField()
    number=models.IntegerField()
    address=models.TextField()
    totalprice=models.CharField(max_length=200)
    paymentmethod=models.CharField(max_length=250)
    transactionid=models.CharField(max_length=250)
    datetime=models.DateTimeField(auto_created=True,auto_now=True)