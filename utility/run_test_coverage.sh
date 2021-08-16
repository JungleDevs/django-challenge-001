#!/usr/bin/env bash
coverage run manage.py test --settings=config.settings --failfast --debug-mode
RESULT=$?
if [ ${RESULT} -eq 0 ]; then
    coverage report
    coverage html
    echo "results at htmlcov/index.html"
else
    return ${RESULT}
fi

