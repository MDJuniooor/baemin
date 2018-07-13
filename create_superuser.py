import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',"baemin.settings")

import django
django.setup()

from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()

try:
    User.objects.create_superuser('admin', '', 'anseotjd')
except IntegrityError:
    print('already created')