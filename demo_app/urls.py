from django.urls import path
from .import views 

urlpatterns = [
    path('', views.homePage, name='home'),
    path('services/', views.servicePage, name='services'),
    path('gallery/', views.galleryPage, name='gallery'),
    path('about/', views.aboutPage, name='about'),
    path('contact/', views.contactPage, name='contact'),
    path('gift/', views.Sgift, name='gift_pack'),
    path('birth/', views.Sbirth, name='birth_pack'),
    path('event/', views.Sevent, name='event_pack'),
    path('photo/', views.Sphoto, name='photo_pack'),
    path('yourplan/', views.Splan, name='plan_pack'),
    path('test/', views.testPage, name='test'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('index/', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('cart2/', views.cart2, name='cartbirth'),
    path('cart3/', views.cart3, name='cartphoto'),
    path('cart4/', views.cart4, name='cartevent'),
    path('bill/', views.bill, name='bill'),

    
    
    
]