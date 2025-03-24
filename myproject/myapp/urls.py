from django.urls import path
from . import views

urlpatterns = [
    path('users/<int:user_id>/works/', views.user_works),
    path('works/<int:work_id>/transfers/', views.transfer_records),
    # ... 其他路由 ...
    path('bind-platform/', bind_platform, name='bind_platform'),
]
