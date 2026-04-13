FROM python:3.11-slim

WORKDIR /app

# install deps first so docker caches this layer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# migrate then start gunicorn - render injects PORT automatically
CMD ["sh", "-c", "python manage.py migrate && gunicorn prompt_nexus.wsgi:application --bind 0.0.0.0:$PORT"]
