# coding=utf-8
import os.path
import sys
import platform

PRODUCTION_HOSTNAME = "tango"

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

ROOT_URLCONF = 'eventhub.urls'

sys.path.append(BASE_PATH + '/apps')

ADMINS = (
    ('Johan Bichel Lindegaard', 'sysadmin@tango.johan.cc'),
)
MANAGERS = ADMINS

DEVELOPMENT_MODE = (platform.node() != PRODUCTION_HOSTNAME)
if DEVELOPMENT_MODE:
    DEBUG = True
    MEDIA_URL = '/media/'
    STATIC_URL = '/static/'
else:
    DEBUG = False
    MEDIA_URL = 'http://media.fairsocialgreen.dk/'
    STATIC_URL = 'http://static.fairsocialgreen.dk/'
    
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
        }
    }

GRAPPELLI_ADMIN_TITLE = "FairSocialGreen"

ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"
INTERNAL_IPS = ['127.0.0.1',]

TEMPLATE_DEBUG = DEBUG

# Static files
MEDIA_ROOT = BASE_PATH + '/../media'
STATICFILES_DIRS = (
    BASE_PATH + '/../static',
)

TIME_ZONE = 'Europe/Copenhagen'
LANGUAGE_CODE = 'da_DK'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

GRAPPELLI_INDEX_DASHBOARD = 'eventhub.dashboard.CustomIndexDashboard'

TEMPLATE_DIRS = (
    BASE_PATH + '/templates/'
)

INSTALLED_APPS = (

    # Third-party
    'taggit',
    'south',
    'sorl.thumbnail',

    'flatblocks',

    'grappelli.dashboard',
    'grappelli',
    
    # Apps
    'events',
    
    # Django
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.markup',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',
)

DATE_FORMAT = "j N Y"
TIME_FORMAT = "H:i"
DATETIME_FORMAT = "j N Y H:i"
PAGINATE_BY = 12

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
    execfile(BASE_PATH + '/settings_local.py')
except IOError:
    sys.stderr.write("\nYou need to copy settings_local.example to settings_local.py and customize it.\n")
    sys.exit(1)