from django.urls import path
from .views import  user_management_list, order_list
from .views import register

urlpatterns = [
    # path('hello/', hello, name='hello'),
    path('user-management/', user_management_list, name='user_management_list'),
    path('register/', register, name='register'),
    path('order-list/', order_list, name='order_list'),
]
