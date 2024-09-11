from django.urls import path
from . import views
from app.views import ProductRegister , Productlist

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('userlogout/',views.userlogout,name='userlogout'),
    path('ProductRegister/',ProductRegister.as_view(),name='ProductRegister'),
    path('Productlist/',Productlist.as_view(),name='Productlist'),
    path('mobilelist/',views.mobilelist,name='mobilelist'),
    path('electroniclist/',views.electroniclist,name='electroniclist'),
    path('showpricerange/',views.showpricerange,name='showpricerange'),
    path('sortingbyprice/',views.sortingbyprice,name="sortingbyprice"),
    path('searchproduct/',views.searchproduct,name="searchproduct"),
    path('showcarts/',views.showcarts,name="cart"),
    path('updatequantity/<int:qv>/<int:productid>',views.updatequantity,name="updatequantity"),
    path('removecart/<int:productid>',views.removecart,name="removecart"),
    path('addtocart/<int:productid>',views.addtocart,name="addtocart"),
    path('payment/',views.payment,name='payment'),
    path('showorders/',views.showorders,name='showorders')
    
]
