from flask import Flask, render_template


def create_app(config_filename=None):
    """
    store config files in instance folder (note that this is to be ignored by
    version control so make sure that instance is in your gitignore)
    """
    app = Flask(__name__, instance_relative_config=True)
    if config_filename != None:
        app.config.from_pyfile(config_filename)
    else:
        app.config.from_mapping(
            RUN_PORT=5500,
            RUN_HOST="0.0.0.0"
        )

    @app.route('/', methods=['GET'])
    def index():
        return render_template('iPortfolio/index.html')

    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        return render_template('contact.html')

    @app.route('/test', methods=['GET'])
    def test():
        return render_template('test.html')

    @app.route('/resume', methods=["GET"])
    def resume():
        return render_template("resume.html")

    @app.route('/portfolio-details.html', methods=["GET"])
    def portfolio():
        return render_template("portfolio-details.html", methods=["GET"])
    

    return app
