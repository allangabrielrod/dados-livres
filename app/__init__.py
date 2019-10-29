from flask import Flask, request
app = Flask(__name__)

from config import Config
app.config.from_object(Config)

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

from flask_migrate import Migrate
migrate = Migrate(app, db)

from flask_babel import Babel, lazy_gettext as _l
babel = Babel(app)
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

from app import routes, models

