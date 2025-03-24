from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Platform(models.Model):
    platform_name = models.CharField(max_length=50)
    api_url = models.CharField(max_length=255)
    auth_token = models.CharField(max_length=255, null=True, blank=True)

class Work(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class TransferRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    source_platform = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name='source_transfers')
    target_platform = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name='target_transfers')
    transfer_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    error_message = models.TextField(null=True, blank=True)