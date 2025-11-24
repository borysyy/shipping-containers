#!/bin/sh

flask db init
flask db migrate
flask db upgrade

exec gunicorn -c gunicorn.conf.py app:app