from django.urls import path
from app import views
from .forms import LoginForm, changepassword, ResetPassword, ResetPAsswordset
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
urlpatterns = [
    path('', views.Home.as_view(),name="home"),
    path('product_detail/<int:id>',views.Product_detail.as_view(), name='product_detail'),
    path('cart/<int:id>/', views.Add_to_cart.as_view(), name='add-to-cart'),
    path('showcart',views.showcart,name='showcart'),
    path('removecart',views.removecart,name='removecart'),
    path('pluscart',views.CartProductQuantity.as_view(),name='plus'),
    path('payment',views.paymentdone,name='paymentdone'),

    path('delitem/int:id>',views.deleteitem,name='delitem'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchane.html',form_class=changepassword,success_url='/profile/'),
         name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('laptop/', views.laptop, name='laptop'),
    path('topwear/', views.topwear, name='topwear'),
    path('btwear/', views.btwear, name='btwear'),
    path('login/',auth_views.LoginView.as_view(authentication_form=LoginForm,template_name="app/login.html"),name="login"),
    path("logout" ,auth_views.LogoutView.as_view(next_page="login"),name='logout'),
    path('registration/', views.Customerregistration.as_view(), name='customerregistration'),
    path('reset-password/',auth_views.PasswordResetView.as_view(
        template_name='app/resetpassword.html',form_class=PasswordResetForm),name='resetpassword'),
    path('reset-password/done/',auth_views.PasswordResetDoneView.as_view(template_name='app/resetpasswordset.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='app/resetpasswordconform.html',form_class=SetPasswordForm),name='password_reset_confirm'),
    path('passwordrest-complete',auth_views.PasswordResetCompleteView.as_view(template_name="app/passwordresetcom.html"),name='password_reset_complete'),
    path('checkout/', views.checkout, name='checkout'),
]
