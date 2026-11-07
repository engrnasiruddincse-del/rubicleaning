#!/usr/bin/env bash
# Run on the server after `git push`:  sudo bash /var/www/rubicleaning/deploy.sh
set -euo pipefail
cd /var/www/rubicleaning

git pull --ff-only
venv/bin/pip install -q -r requirements.txt
venv/bin/python manage.py migrate --noinput
venv/bin/python manage.py collectstatic --noinput -v 0
venv/bin/python manage.py build_translations

chown -R www-data:www-data /var/www/rubicleaning
systemctl restart rubicleaning-backend
echo "Deployed $(git log -1 --format='%h %s')"
