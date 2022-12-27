from flask import Flask, render_template
from livereload import Server
from .portfolio_site import create_app
from . import dev_config


if __name__ == '__main__':
    app = create_app()
    server = Server(app.wsgi_app)
    # server.watch('./templates/*')
    server.serve(host='0.0.0.0')