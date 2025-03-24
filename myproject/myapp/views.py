from django.http import JsonResponse
from .models import User, Platform, Work, TransferRecord
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login


@csrf_exempt
def user_works(request, user_id):
    if request.method == 'GET':
        try:
            user = User.objects.get(pk=user_id)
            works = Work.objects.filter(user=user)
            work_list = [{
                'title': work.title,
                'platform': work.platform.platform_name,
                'created_at': work.created_at
            } for work in works]
            return JsonResponse({'works': work_list})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)


@csrf_exempt
def bind_platform(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({'error': '请先登录'}, status=401)

        data = json.loads(request.body)
        platform_name = data.get('platform_name')
        auth_token = data.get('auth_token')

        if not platform_name or not auth_token:
            return JsonResponse({'error': '缺少必要参数'}, status=400)

        platform, created = Platform.objects.get_or_create(
            platform_name=platform_name,
            defaults={'auth_token': auth_token}
        )

        # 将平台与当前用户关联
        platform.user = request.user
        platform.save()

        return JsonResponse({'message': '绑定成功'})

    return JsonResponse({'error': '无效的请求方法'}, status=400)

@csrf_exempt
def transfer_records(request, work_id):
    if request.method == 'GET':
        try:
            work = Work.objects.get(pk=work_id)
            records = TransferRecord.objects.filter(work=work)
            record_list = [{
                'source_platform': record.source_platform.platform_name,
                'target_platform': record.target_platform.platform_name,
                'status': record.status,
                'transfer_time': record.transfer_time
            } for record in records]
            return JsonResponse({'transfer_records': record_list})
        except Work.DoesNotExist:
            return JsonResponse({'error': 'Work not found'}, status=404)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 创建用户时自动创建UserProfile
            UserProfile.objects.create(
                user=user,
                user_level='普通用户',
                user_status='正常',
                user_balance=0.00
            )
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # 重定向到主页
        else:
            return render(request, 'registration/login.html', {'error': '用户名或密码错误'})
    return render(request, 'registration/login.html')