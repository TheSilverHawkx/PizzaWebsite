import os
from flask import Flask
from . import db

def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)


    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    # Initialize DB
    from . import db
    db.init_app(app)

    # Import authentication blueprint
    from . import auth
    app.register_blueprint(auth.bp)

    # Import Blog blueprint
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    # Import Orders blueprint
    from . import orders
    app.register_blueprint(orders.bp)

    return app
