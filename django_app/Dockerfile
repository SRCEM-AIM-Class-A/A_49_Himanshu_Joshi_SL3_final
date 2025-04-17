FROM python

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run migrations and create superuser
RUN python manage.py makemigrations
RUN python manage.py migrate

# Create a superuser script
RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin') if not User.objects.filter(username='admin').exists() else None" > create_superuser.py

# Execute the script
RUN python manage.py shell < create_superuser.py

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]