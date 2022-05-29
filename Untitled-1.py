'''
プロジェクト・設定・アプリを作成
$ mkdir project
$ cd project
$ django-admin startproject config .
$ py manage.py startapp app
'''

# project / config / settings.py
from pathlib import *

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-m#(d_y73-h&evpgch)54yv0_&a9$%#r))391)y!g$ixtnii$&o'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app.apps.AppConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ]
        }
    }
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3'
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'
    }
]

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# project / app / views.py
from django.shortcuts import render
from django.views import generic

class IndexView(generic.TemplateView):
    template_name = 'index.html'

# project / app / urls.py
from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]

# project / config / urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
]

# project / app / templates / index.html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>title</title>
    </head>
    <body>
        <p>Hello World</p>
    </body>
</html>

'''
管理者登録
$ cd project
$ py manage.py createsuperuser
Username (leave blank to use 'root'): admin
Email address: admin@example.com
Password: ***password***
Password (again): ***password***
'''

'''
サーバを起動
$ cd project
$ py manage.py runserver
'''

'''
サーバを停止
ctrl + c
'''