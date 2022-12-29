from flask import Flask, render_template
from .recursive import recursive_indexer


def create_app(config_filename):
    """
    store config files in instance folder (note that this is to be ignored by
    version control so make sure that instance is in your gitignore)
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)

    @app.route('/', methods=['GET'])
    def index():
        image_path = "portfolio_site/static/img"
        desc_path = "portfolio_site/static/descriptions"
        ignored = ['favicons', 'hero', '.DS_Store']
        projects = recursive_indexer.get_projects_for_display(image_path, desc_path, ignored)
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

    @app.route('/resume', methods=["GET"])
    def resume():
        return render_template("resume.html")
    

    return app