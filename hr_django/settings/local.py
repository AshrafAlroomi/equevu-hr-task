import os

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DB_HOST = os.environ.get('DB_HOST', 'localhost')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hr-system',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': DB_HOST,
        'PORT': '5432',
    }
}
