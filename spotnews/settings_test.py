from .settings import *  # noqa: F403, F405

MEDIA_URL = ''
MEDIA_ROOT = BASE_DIR / 'tests'  # noqa: F405
STORAGE = {"default": 'django.core.files.storage.FileSystemStorage'}
