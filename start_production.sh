#!/bin/bash

. portfolio_venv/bin/activate
waitress-serve --call 'portfolio_site:create_app'