from portfolio_site import create_app
from livereload import Server

def live_config():
    """
    for usage with livereload
    note that if you use this function, changing any python file
    will crash the program completely and you'll have to restart the app.
    """
    app = create_app("config.py")
    server = Server(app.wsgi_app)
    server.serve()

def regular_dev():
    """
    No front end changes will show up when using this function, use live_config for that
    """
    app = create_app("dev.py")
    app.config.update("TEMPLATES_AUTO_RELOAD")
    app.run(host="0.0.0.0", port=5500)

if __name__ == '__main__':
    live_config()