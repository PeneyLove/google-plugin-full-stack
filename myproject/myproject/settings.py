WSGI_APPLICATION = 'myproject.wsgi.application'
INSTALLED_APPS = [
    # ...
    'corsheaders',
]

# 修正点1：确保中间件顺序正确
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # 必须放在CommonMiddleware之前
    'django.middleware.common.CommonMiddleware',
]

# 修正点2：添加更完整的CORS配置
CORS_ALLOWED_ORIGINS = [
    "https://www.tiktok.com",
    "http://localhost:3000",    # 开发服务器地址
    "chrome-extension://扩展ID"  # 替换为实际扩展ID
]

# 新增配置（请求头和方法）
CORS_ALLOW_HEADERS = [
    'content-type',
    'authorization',
]
CORS_ALLOW_METHODS = [
    'GET',
    'POST'
]

# 允许访问的主机
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'your-domain.com',  # 替换为你的实际域名
    '192.168.218.50'   # 替换为你的实际IP地址
]
# DEBUG = True