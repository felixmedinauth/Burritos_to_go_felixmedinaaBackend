"""
Django settings for burritos_project project.
... (Notas originales)
"""

from pathlib import Path
import os # <-- ¡AÑADIDO! Necesario para STATIC_ROOT

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--xlh$a9igpj$-w&q$d8$w57elq6t#ea1cjn1ph^i%@zakc3^b5'

# SEGURIDAD Y RENDIMIENTO EN PYTHONANYWHERE
# Punto 7: DEBUG = False en producción.
DEBUG = False 

# Punto 7: Configurar tu dominio en ALLOWED_HOSTS.
ALLOWED_HOSTS = ['felixmedinaabackend.pythonanywhere.com', '127.0.0.1']

CORS_ALLOW_ALL_ORIGINS = True


# Application definition
# ... (INSTALLED_APPS y MIDDLEWARE sin cambios)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'burritos_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'burritos_project.wsgi.application'


# Database - CONFIGURACIÓN PARA MYSQL EN PYTHONANYWHERE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # Nombre de la BD en PythonAnywhere
        'NAME': 'felixmedinaaback$default', 
        # USUARIO DE MYSQL CORREGIDO:
        'USER': 'felixmedinaaback', 
        # Contraseña de MySQL
        'PASSWORD': 'medina1x', 
        # Host: El estándar para PythonAnywhere
        'HOST': 'felixmedinaabackend.mysql.pythonanywhere-services.com', 
        'PORT': '3306'
    }
}

AUTH_USER_MODEL = "core.Usuario"

# ... (El resto de la configuración sin cambios)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Punto 7: Donde se recopilarán los archivos estáticos en producción.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'