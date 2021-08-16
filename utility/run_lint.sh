#!/usr/bin/env bash

flake8 --exclude=*env*,.tox,.git,*/migrations/*,*/static/CACHE/*,docs,node_modules
