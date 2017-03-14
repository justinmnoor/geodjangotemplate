import json
import random


def get_random_string(length=50,
                      allowed_chars='abcdefghijklmnopqrstuvwxyz'
                                    'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
                                    '!@#$%^&*()'):
    """
    Returns a securely generated random string.
    The default length of 12 with the a-z, A-Z, 0-9 character set returns
    a 71-bit value. log_2((26+26+10)^12) =~ 71 bits
    See: https://github.com/django/django/blob/master/django/utils/crypto.py
    Non-alphanumeric symbols were added by me.
    """

    return ''.join(random.choice(allowed_chars) for i in range(length))


SECRET_KEY = get_random_string()


dj_envars = {
        
        "FILENAME": "dj_config.json",
        "DJANGO_ALLOWED_HOSTS": "*",
        "DJANGO_SECRET_KEY": SECRET_KEY,
        "DJANGO_SETTINGS_MODULE": "{{cookiecutter.project_slug}}.settings.production"

}


with open('{{cookiecutter.project_slug}}/config/dj_config.json', 'w') as f:  
    json.dump(dj_envars, f, indent=4)
