from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.models import *
# Create your views here.

def data(request):
    return HttpResponse ("<h1>This is my first website</h1>")

def index(request):
    a=Category.objects.all()
    return render(request,'index.html',{'data':a})

def productall(request):
    a=product.objects.all()
    return render (request,'product.html',{'data':a})

def productfilter(request,id):
    a=product.objects.filter(category=id)
    return render (request,'product.html',{'data':a})

def productget(request,id):
    if 'm' in request.session:
        m=request.session['m']
        del request.session['m']
    else:
        m=""
    a=product.objects.get(id=id)
    return render(request,'product_detail.html',{'data':a,'m':m})

def register(request):
    return render(request,'register.html')

def login(request):
    if request.method=="POST": 
        email1=request.POST['email']
        pass1=request.POST['password']
        try:
            user=userregister.objects.get(email=email1,password=pass1)
            if user:
                request.session['email']=user.email
                request.session['id']=user.pk
                print(request.session['id'],request.session['email'])
                return redirect('home')
            else:
                return render(request,"login.html",{'m':'invalid data enter'})
        except:
            return render(request,"login.html",{'m':'invalid data enter'})
    return render(request,"login.html")

def logout(request):
    if 'email' in request.session:
        del request.session['email']
        del request.session['id']
        return redirect('login1')
    else:
        return redirect('login1')

def register(request):
    if request.method=="POST":
        name1=request.POST['name']
        email1=request.POST['email']
        number1=request.POST['number']
        address1=request.POST['address']
        pass1=request.POST['password']
        user= userregister(name=name1,email=email1,number=number1,address=address1,password=pass1)
        print(userregister.objects.filter(email=email1).exists())
        data=userregister.objects.filter(email=email1)
        if len(data)==0:
            user.save()
            return redirect(login)
        else:
            return render(request,"register.html",{'m':'user already exists'})
    return render(request,"register.html")

def contact1(request):
    if request.method=="POST":
        name2= request.POST['nm']
        email2= request.POST['emil']
        number2= request.POST['num']
        address2= request.POST['location']
        comment1=request.POST['comment']
        data=contactus(name=name2,email=email2,number=number2,address=address2,comment=comment1)
        data.save()
    return render(request,'contact_us.html')


def profile(request):
    if 'email' in request.session:
        userdata=userregister.objects.get(email=request.session['email'])
        if request.method=="POST":
           userdata.name=request.POST['name']
           userdata.number=request.POST['number']
           userdata.address=request.POST['address']
           userdata.save()
           return render(request,'profile.html',{'user':userdata,'m':'profile updated'})
        return render(request,'profile.html',{'user':userdata})
    else:
        return redirect('login1')
    
def changepass(request):
    if 'email' in request.session:
        userdata=userregister.objects.get(email=request.session['email'])
        if request.method=="POST":
           old=request.POST['oldpass']
           newpass=request.POST['password']
           c_pass=request.POST['password1']
           if userdata.password==old:
               if newpass==c_pass:
                   userdata.password=newpass
                   userdata.save()
                   return render(request,'changepass.html',{'user':userdata,'m':'Password Updated..'})
               else:
                   return render(request,'changepass.html',{'user':userdata,'m':'Password Missmatch'})
           else:
               return render(request,'changepass.html',{'user':userdata,'m':'Incorrect Old Password'})
        return render(request,'changepass.html',{'user':userdata})
    else:
        return redirect('login1')

def vendorlogin(request):
    if request.method=="POST":
        email1=request.POST['email']
        pass1=request.POST['password']
        try:
            Vendor=Vendorregister.objects.get(email=email1,password=pass1)
            if Vendor:
                request.session['Vendoremail']=Vendor.email
                request.session['Vendorid']=Vendor.pk
                return redirect('home')
            else:
                return render(request,'login.html',{'m':"invalid userid and password"})
        except:
            return render(request,'login.html',{'m':"invalid data enter"})
    return render(request,'login.html')

def vendorlogout(request):
    if 'Vendoremail' in request.session:
        del request.session['Vendoremail']
        del request.session['Vendorid']
        return redirect('Vendorlogin')
    else:
        return redirect('Vendorlogin')

def vendorregister(request):
    if request.method=="POST":
        name1=request.POST['name']
        email1=request.POST['email']
        number1=request.POST['number']
        address1=request.POST['address']
        pass1=request.POST['password']
        Vendor=Vendorregister(name=name1,email=email1,number=number1,address=address1,password=pass1)
        
        if len(Vendorregister.objects.filter(email=email1))==0:
            Vendor.save()
            return redirect('Vendorlogin')
        else:
            return render(request,'register.html',{'m':"Vendor alredy exist"})
    return render(request,'register.html')

def add_product(request):
    if 'Vendoremail' in request.session:
        a=Category.objects.all()
        if request.method=="POST" and request.FILES['img']:
            pro=product()
            b=Category.objects.get(id=request.POST['category'])
            pro.vendorid=request.session['Vendorid']
            pro.category=b
            pro.name=request.POST['name']
            pro.quantity=request.POST['quantity']
            pro.discription=request.POST['disc']
            pro.image=request.FILES['img']
            pro.price=request.POST['price']
            pro.save()
        return render(request,'addproduct.html',{'data':a})
    else:
        return redirect('Vendorlogin')
    
def updateproduct(request,id):
    if 'Vendoremail' in request.session:
        a=product.objects.get(id=id)
        b=Category.objects.all()
        return render(request,'updateproduct.html',{'a':a,'data':b})
    else:
        return redirect("vendorlogin")
    
def addcart(request):
    if 'email' in request.session:
        if request.POST:
            try:
                data=cart()
                data.userid=request.session['id']
                data.productid=request.POST['productid']
                x=request.POST['productid']
                a=product.objects.get(id=x)
                data.vendorid=a.vendorid
                data.orderid="0"
                data.quantity=request.POST['quantity']
                data.totalprice=a.price*int(data.quantity)
                a=cart.objects.filter(productid=x) & cart.objects.filter(orderid="0")
                if len(a)==0:
                    data.save()
                    request.session['m']="product added"
                    return redirect('product_get',x)
                else:
                    request.session['m']="product already exists"
                    return redirect('product_get',x)
            except:
                request.session['m']="enter the valid quantity"
                return redirect('product_get',x)

    else:
        return redirect('login1')
    

def cartpage(request):
    if 'email' in request.session:
        data=cart.objects.filter(userid=request.session['id'])
        d=[]
        final=0
        for i in data:
            final+=int(i.totalprice)
            prodict={}
            prodata=product.objects.get(id=i.productid)
            prodict['name']=prodata.name
            prodict['id']=i.pk
            prodict['img']=prodata.image
            prodict['price']=prodata.price
            prodict['quantity']=i.quantity
            prodict['totalprice']=i.totalprice
            d.append(prodict)

        return render(request,'cart.html',{'prolist':d,'final':final,'noitem':len(d)})
    else:
        return redirect('login1')
    
def removeitem(request,id):
    if 'email' in request.session:
        data=cart.objects.get(id=id)
        data.delete()
        return redirect('cart2')
    else:
        return redirect('login1')
    
def removeallitem(request):
    print(1111)
    if 'email' in request.session:
        data=cart.objects.filter(userid=request.session['id']) and cart.objects.filter(orderid="0")
        print(1111)
        data.delete()
        return redirect('cart2')
    else:
        return redirect('login1')

def shipping(request):
    if 'email' in request.session:
        userdata=userregister.objects.get(id=request.session['id'])
        data=cart.objects.filter(userid=request.session['id']) and cart.objects.filter(orderid="0")
        final=0
        for i in data:
            final+=int(i.totalprice)
        if request.POST:
        
            request.session['name']=request.POST['name']
            request.session['email']=request.POST['email']
            request.session['number']=request.POST['number']
            request.session['address']=request.POST['address']
            request.session['price']=request.POST['final']
            request.session['paymentmethod']="Razorpay"
            return redirect('razorpayView')
        return render(request,'shipping.html',{'final':final,'userdata':userdata})
    else:
        return redirect('login1')
    
def success(request):
    if 'email' in request.session:
        return render(request,'success.html')
    else:
        return redirect('login1')



import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest


RAZOR_KEY_ID = 'rzp_test_zL4x6es7f6MDMC'
RAZOR_KEY_SECRET = '90zx8auoMY7ynohwHWX6LW7h'
client = razorpay.Client(auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))

def razorpayView(request):
    currency = 'INR'
    amount = int(request.session['price'])*100
    # Create a Razorpay Order
    razorpay_order = client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'http://127.0.0.1:8000/paymenthandler/'    
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url    
    return render(request,'razorpayDemo.html',context=context)

@csrf_exempt
def paymenthandler(request):
    # only accept POST request.
    if request.method == "POST":
        try:
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')

            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = client.utility.verify_payment_signature(
                params_dict)
            
            amount = int(request.session['price'])*100  # Rs. 200
            # capture the payemt
            client.payment.capture(payment_id, amount)

            #Order Save Code
            orderModel = Order()
            orderModel.userid=request.session['id']
            orderModel.name=request.session['name']
            orderModel.email=request.session['email']
            orderModel.number=request.session['number']
            orderModel.address=request.session['address']
            orderModel.totalprice = request.session['price']
            orderModel.paymentmethod = request.session['paymentmethod']
            orderModel.transactionid = payment_id
            orderModel.save()
            orderdata=Order.objects.latest('id')
            data=cart.objects.filter(userid=request.session['id']) and cart.objects.filter(orderid="0")
            for i in data:
                productdata=product.objects.get(id=i.productid)
                productdata.quantity-=int(i.quantity)
                productdata.save()
                i.orderid=orderdata.pk
                i.save()
            del request.session['name']
            del request.session['number']
            del request.session['address']
            del request.session['price']
            del request.session['paymentmethod']
        
            return redirect('success1')
            
        except:
            print("Hello")
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
        print("Hello1")
       # if other than POST request is made.
        return HttpResponseBadRequest()

def ordertable(request):
    if 'email' in request.session:
        myorder=Order.objects.filter(userid=request.session['id'])

        return render(request,'ordertable.html',{'myorder':myorder})
    else:
        return redirect('login1')

def orderdetails(request,id):
    if 'email' in request.session:
        myorder=Order.objects.get(id=id)
        cartdata=cart.objects.filter(orderid=myorder.pk)
        d=[]
        final=0
        for i in cartdata:
            prodict={}
            prodata=product.objects.get(id=i.productid)
            prodict['name']=prodata.name
            prodict['image']=prodata.image
            prodict['dis']=prodata.discription
            prodict['quantity']=i.quantity
            prodict['totalprice']=i.totalprice
            d.append(prodict)

        return render(request,'orderdetails.html',{'myorder':myorder,'prolist':d})
    else:
        return redirect('login1') 
    
def vendor_order(request):
    if 'Vendoremail' in request.session:
        myorder=cart.objects.filter(vendorid=request.session['Vendorid'])
        d=[]
        for i in myorder:
            if i.orderid != "0":
                prodict={}
                prodata=product.objects.get(id=i.productid)
                orderdata=Order.objects.get(id=i.orderid)
                userdata=userregister.objects.get(id=i.userid).name
                prodict['name']=prodata.name
                prodict['img']=prodata.img
                prodict['transactionid']=orderdata.transactionid
                prodict['date']=orderdata.datetime
                prodict['user']=userdata
                prodict['quantity']=i.quantity
                prodict['totalprice']=i.totalprice
                d.append(prodict)            
        return render(request,'vendororder.html',{'prolist':d})
    else:
        return redirect('Vendorlogin')