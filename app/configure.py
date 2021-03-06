import os

workers = int(os.environ.get('GUNICORN_PROCESSES', '3'))
threads = int(os.environ.get('GUNICORN_THREADS', '1'))

forwarded_allow_ips = '*'
secure_scheme_headers = {'X-Forwarded-Proto': 'https'}

DATABASE_URI = 'postgresql://localhost/quality_metrics_reg'
SQLALCHEMY_TRACK_MODIFICATIONS = False


DEBUG = True
