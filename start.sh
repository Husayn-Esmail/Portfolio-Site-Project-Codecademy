#!/bin/bash
# setup for the server
source portfolio_venv/bin/activate
export FLASK_APP="portfolio_site"
export FLASK_DEBUG="True"
export FLASK_ENV="development"
export TEMPLATES_AUTO_RELOAD="True"
export FLASK_RUN_EXTRA_FILES="portfolio_site/static/css/style.css:portfolio_site/templates/resume.html"
export FLASK_RUN_HOST="0.0.0.0"
export FLASK_RUN_PORT="5500"
echo $FLASK_RUN_EXTRA_FILES
python3 -m flask run
# python3 portfolio_site/__init__.py
