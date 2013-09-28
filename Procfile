web: sh -c 'cd outpatient && python manage.py collectstatic --noinput --settings='outpatient.settings.production' && gunicorn outpatient.wsgi'
