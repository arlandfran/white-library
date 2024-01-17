set -o errexit
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py makemigrations && python manage.py migrate