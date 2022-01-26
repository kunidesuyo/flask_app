from pathlib import Path
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from apps.config import config
from flask_login import LoginManager

# SQLAlchemyをインスタンス化する
db = SQLAlchemy()

csrf = CSRFProtect()

# LoginManagerをインスタンス化
login_manager = LoginManager()
# login_view属性に未ログイン時にリダイレクトするエンドポイントを指定する
login_manager.login_view = "auth.signup"
# login_message属性にログイン後に表示するメッセージを指定する
# ここではなにも表示しないよう空を指定する
login_manager.login_message = ""


def create_app(config_key):
    app = Flask(__name__)
    # アプリのコンフィグ設定をする
    app.config.from_object(config[config_key])

    csrf.init_app(app)

    # SQLAlchemyとアプリを連携する
    db.init_app(app)
    # Migrateとアプリを連携する
    Migrate(app, db)
    # login_managerをアプリケーションと連携する
    login_manager.init_app(app)

    from apps.crud import views as crud_views

    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    # これから作成するauthパッケージからviewsをimportする
    from apps.auth import views as auth_views
    # register_blueprintを使いviewsのauthをアプリへ登録する
    app.register_blueprint(auth_views.auth, url_prefix="/auth")

    return app


