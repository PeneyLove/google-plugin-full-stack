from django.http import JsonResponse
from .models import UserProfile, Order
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # 假设你有一个名为 'login' 的 URL 路径
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@csrf_exempt
def user_management_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        user_list = []
        for user in users:
            try:
                profile = UserProfile.objects.get(user=user)
                user_info = {
                    'username': user.username,
                    'user_level': profile.user_level,
                    'user_status': profile.user_status,
                    'user_balance': str(profile.user_balance)
                }
                user_list.append(user_info)
            except UserProfile.DoesNotExist:
                pass
        return JsonResponse({'users': user_list})
    return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        order_list = []
        for order in orders:
            order_info = {
                'product_name': order.product_name,
                'order_number': order.order_number,
                'merchant_number': order.merchant_number,
                'purchase_time': str(order.purchase_time),
                'order_status': order.order_status,
                'username': order.user.username
            }
            order_list.append(order_info)
        return JsonResponse({'orders': order_list})
    return JsonResponse({'error': 'Invalid request method'}, status=400)
