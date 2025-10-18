#!/usr/bin/env bash
set -o errexit

cd lab
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate