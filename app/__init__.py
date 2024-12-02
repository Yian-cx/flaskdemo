from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import pymysql

# 初始化扩展
db = SQLAlchemy()
migrate = Migrate()
pymysql.install_as_MySQLdb()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # 加载配置

    # 初始化扩展
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # 注册所有的蓝图
    register_blueprints(app)

    return app


def register_blueprints(app):
    """
    注册所有的蓝图，使用列表和循环简化注册过程。
    """
    blueprints = [
        ('app.routes.home', '/'),
        ('app.routes.books', '/api/books'),
        ('app.routes.users', '/api/users'),
        ('app.routes.reviews', '/api/reviews'),
        ('app.routes.categories', '/api/categories'),
        ('app.routes.logs', '/api/logs')
    ]

    for module_name, url_prefix in blueprints:
        module = __import__(module_name, fromlist=['bp'])
        app.register_blueprint(module.bp, url_prefix=url_prefix)
