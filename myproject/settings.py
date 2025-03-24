MIDDLEWARE = [
    # ... 其他中间件 ...
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

INSTALLED_APPS = [
    # ... 其他应用 ...
    'django.contrib.auth',
    'django.contrib.sessions',
]

ROOT_URLCONF = 'myproject.urls'