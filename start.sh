#!/bin/bash
# setup for the server
export FLASK_APP=portfolio-site
export FLASK_ENV=development
export FLASK_RUN_PORT=5500
export FLASK_DEBUG=True
export FLASK_RUN_EXTRA_FILES="./static/css/"
export FLASK_RUN_HOST=0.0.0.0
export TEMPLATES_AUTO_RELOAD=True
echo $FLASK_RUN_EXTRA_FILES
flask run
# python3 portfolio-site/__init__.py