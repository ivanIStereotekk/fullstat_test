echo "Apply database migrations and superuser"

python manage.py makemigrations

python manage.py migrate

echo "from django.contrib.auth.models import Person; Person.objects.create_superuser($SUPER_USER,$SUPER_USER_EMAIL,$SUPER_USER_PASS)" | python manage.py shell

