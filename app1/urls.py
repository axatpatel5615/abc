from django.urls import path,include
# from app1.views import data,index,productall,productfilter,login,productget
from app1.views import *

urlpatterns =[
    path('data/',data),
    path('',index,name="home"),
    path('product-all/',productall,name='productall'),
    path('product-filter/<int:id>/',productfilter,name='product_filter'),
    path('login/',login,name='login1'),
    path('register/',register,name="register1"),
    path('product-get/<int:id>/',productget,name="product_get"),
    path('logout/',logout,name='logout1'),
    path('profile/',profile,name='profile1'),
    path('contactus/',contact1,name='contact1'),
    path('changepass/',changepass,name='changepass1'),
    path('Vendor-login/',vendorlogin,name="Vendorlogin"),
    path('vendor-register/',vendorregister,name='vendorregister'),
    path('vendor-logout/',vendorlogout,name="vendorlogout"),
    path('add_product/',add_product,name="addproduct1"),
    path('success/',success,name="success1"),
    path('updateproduct/<int:id>/',updateproduct,name="updateproduct1"),
    path('add-cart/',addcart,name="addcart1"),
    path('cart/',cartpage,name="cart2"),
    path('shipping',shipping,name="shipping1"),
    path('removeitem/<int:id>/',removeitem,name="removeitem"),
    path('removeallitem/',removeallitem,name="removeallitem1"),
    path('razorpayView/',razorpayView,name='razorpayView'),
    path('paymenthandler/',paymenthandler,name='paymenthandler'),
    path('order-table/',ordertable,name="ordertable"),
    path('order-details/<int:id>/',orderdetails,name="orderdetails2"),
    path('vendor-order/',vendor_order,name="vendor_order1")

]