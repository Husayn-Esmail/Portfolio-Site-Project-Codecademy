from email.mime import image
from flask import Flask, render_template
import os
from recursive.recursive_indexer import get_projects_for_display, index_images

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )
    # not setting up a database
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/', methods=['GET'])
    def index():
        image_path = "portfolio-site/static/img"
        desc_path = "portfolio-site/static/descriptions"
        projects = get_projects_for_display(image_path, desc_path)
        # the projects out of read_images are not json serializable, must be
        # converted first.
        json_projects = []
        for project in projects:
            json_projects.append(project.to_json())
        data = json_projects
        return render_template('index.html', data=data)

    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        return render_template('contact.html')

    @app.route('/test', methods=['GET'])
    def test():
        return render_template('test.html')

    return app