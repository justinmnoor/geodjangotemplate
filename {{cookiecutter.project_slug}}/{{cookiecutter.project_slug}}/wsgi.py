import os

from django.core.wsgi import get_wsgi_application


# WSGI CONFIGURATION
# =================================================================================================

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{cookiecutter.project_slug}}.settings.production")

application = get_wsgi_application()

