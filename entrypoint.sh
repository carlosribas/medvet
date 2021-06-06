#!/bin/sh
set -e

SECRET_KEY=${SECRET_KEY:-$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')}

# Add settings_local file
if [ -f /app/medvet/settings_local.py ]
then
	echo "INFO: settings_local.py file already provisioned"
else
	echo "INFO: Creating settings_local.py file"
	cat <<-EOF > /app/medvet/settings_local.py
		SECRET_KEY = "$SECRET_KEY"
		DEBUG = True
		STATIC_ROOT = '/app/statifiles'
		DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'db',
            'PORT': 5432,
        }
    }
	EOF
fi

exec "$@"