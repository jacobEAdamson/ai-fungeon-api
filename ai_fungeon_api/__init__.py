import os
from flask import Flask
from flask_cors import CORS

def create_app(test_config=None): 
    app = Flask(__name__, instance_relative_config=True, static_url_path='/static')
    CORS(app) # allow CORS for all domains on all routes.
    
    # create and configure the app
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

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

    from ai_fungeon_api.views.root import root_blueprint
    app.register_blueprint(root_blueprint)

    return app
