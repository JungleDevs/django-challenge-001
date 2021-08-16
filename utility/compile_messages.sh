#!/usr/bin/env bash

python manage.py makemessages -a --extension html,txt,py --ignore="*env*" --locale=pt_BR

if [ $# -eq 0 ]; then
  read -p "Waiting.. Press any key to start compiling... " -n1 -s
fi

python manage.py compilemessages --locale=en
if [ "$(uname)" == "Darwin" ]; then
  sed -i '' '/POT-Creation-Date/d' locale/en/LC_MESSAGES/django.po
  sed -i '' '/^#/d' locale/en/LC_MESSAGES/django.po

#  python manage.py compilemessages --locale=es
#  sed -i '' '/POT-Creation-Date/d' locale/es/LC_MESSAGES/django.po
#  sed -i '' '/^#/d' locale/es/LC_MESSAGES/django.po

  python manage.py compilemessages --locale=pt_BR
  sed -i '' '/POT-Creation-Date/d' locale/pt_BR/LC_MESSAGES/django.po
  sed -i '' '/^#/d' locale/pt_BR/LC_MESSAGES/django.po
else
  sed -i '/POT-Creation-Date/d' locale/en/LC_MESSAGES/django.po
  sed -i '/^#/d' locale/en/LC_MESSAGES/django.po

#  python manage.py compilemessages --locale=es
#  sed -i '/POT-Creation-Date/d' locale/es/LC_MESSAGES/django.po
#  sed -i '/^#/d' locale/es/LC_MESSAGES/django.po

  python manage.py compilemessages --locale=pt_BR
  sed -i '/POT-Creation-Date/d' locale/pt_BR/LC_MESSAGES/django.po
  sed -i '/^#/d' locale/pt_BR/LC_MESSAGES/django.po
fi

