#!/usr/bin/env bash
./conf/wait-for-it.sh -t 30 db:5432
python manage.py runserver 0.0.0.0:8000