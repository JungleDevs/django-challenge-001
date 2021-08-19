#!/bin/bash

# Start Gunicorn processes
echo "Setting up server...."
python3 ./manage.py runserver 0.0.0.0:8000 --settings=config.settings

