web: sh -c 'cd outpatient && python manage.py collectstatic --noinput --settings='outpatient.settings.production'; cd outpatient && gunicorn outpatient.wsgi'
