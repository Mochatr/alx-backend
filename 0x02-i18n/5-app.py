#!/usr/bin/env python3
"""
Basic Flask application
with Babel integration for i18n
and user login emulation
"""

from flask import Flask, request, render_template, g
from flask_babel import Babel, _


class Config:
    """
    Configuration class for Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "Us/Central"},
    1: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    1: {"name": "Teletubby", "locale": "None", "timezone": "Europe/London"},
}


def get_user():
    """
    Retrieve a user based on the login_as parameter.
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (ValueError, TypeError):
        return None


@app.before_request
def before_request():
    """
    Set the current user as a global
    before each request
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    Select the best match language
    for the user or usr the 'locale' URL
    parameter.
    """
    if g.user and g.user.get("locale") in app.config['LANGUAGES']:
        return g.user.get("locale")
    return request.args.get("locale") or request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Render the index page."""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(debug=True)
