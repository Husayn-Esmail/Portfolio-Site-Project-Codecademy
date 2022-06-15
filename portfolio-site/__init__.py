from flask import Flask, render_template
import os
from recursive.recursive_indexer import read_images

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
        projects = []
        path = "portfolio-site/static/img"
        read_images(projects, path)
        project_langs = []
        project_projects = []
        for project in projects:
            project_langs.append(project.get_prog_language())
            project_projects.append(project.get_projects())

        data = project_langs
        a_list = project_projects
        return render_template('index.html', data=data, a_list=a_list)

    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        return render_template('contact.html')

    @app.route('/test', methods=['GET'])
    def test():
        return render_template('test.html')

    return app