# Importaciones necesarias
import os
from pathlib import Path

# Define la ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración de la ubicación de los archivos estáticos
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Configuración de la clave secreta (¡asegúrate de cambiarla en producción!)
SECRET_KEY = 'django-insecure--53y#p+pbu)c(+v#(ucuv!2+9$k2_w9)cif$8f=l-2ht4hy&n$'

# Habilitar o deshabilitar el modo de depuración (DEBUG) según sea necesario
DEBUG = True

# Lista de hosts permitidos en producción (dejar en blanco para desarrollo)
ALLOWED_HOSTS = []

# Configuración de las aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
]

# Middleware utilizado en la aplicación
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de la URL raíz de la aplicación
ROOT_URLCONF = 'proyecto1.urls'

# Configuración de las plantillas de la aplicación
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuración de la aplicación WSGI
WSGI_APPLICATION = 'proyecto1.wsgi.application'

# Configuración de la base de datos (utiliza SQLite en este caso)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configuración de las validaciones de contraseña
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Configuración de la internacionalización
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Configuración de archivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Ruta donde se almacenarán los archivos estáticos recolectados

# Tipo de campo clave primaria predeterminado
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
