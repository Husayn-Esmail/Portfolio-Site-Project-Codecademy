#!/bin/bash
# setup for the server
source portfolio_venv/bin/activate
export FLASK_APP="portfolio-site"
export FLASK_DEBUG="True"
export FLASK_ENV="development"
export TEMPLATES_AUTO_RELOAD="True"
export FLASK_RUN_EXTRA_FILES="portfolio-site/static/css/style.css:portfolio-site/templates/resume.html"
export FLASK_RUN_HOST="0.0.0.0"
export FLASK_RUN_PORT="5500"
echo $FLASK_RUN_EXTRA_FILES
python3 -m flask run
# python3 portfolio-site/__init__.py
