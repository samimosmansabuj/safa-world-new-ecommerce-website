from django.urls import path
from .views import *

urlpatterns = [
    path('my-account/', my_account, name='my_account'),
    path('edit-my_account/<int:id>/', edit_my_account, name='edit_my_account'),
    path('track-order/', track_order, name='track_order'),
    path('my-order/', my_order, name='my_order'),
    path('order-details/', order_details, name='order_details'),
    
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    
    path('registration/', registration, name='registration'),
    path('otp-verify-account/<int:id>/', otp_verify_account, name='otp_verify_account'),
    path('token-verify-account/<int:id>/<auth_token>/', token_verify_account, name='token_verify_account'),
    
    path('forget-password/', forget_password, name='forget_password'),
    path('change-password/', change_password, name='change_password'),
]