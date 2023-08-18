"""
__init__.py - 应用的初始化

Author: kayotin
Date 2023/8/4
"""

import os

from flask import Flask
from flask import send_from_directory


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # 欢迎界面
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/favicon.ico')
    def favicon():
        """设置网站图标"""
        return send_from_directory(os.path.join(app.root_path, 'static/pic'),
                                   'favicon.ico', mimetype='image/vnd.microsoft.icon')

    from hanayo_hr import index
    app.register_blueprint(index.bp)
    app.add_url_rule('/', endpoint='index')

    return app


if __name__ == '__main__':
    my_app = create_app()
    my_app.run(debug=True)
