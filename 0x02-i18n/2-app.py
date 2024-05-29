#!/usr/bin/env python3
"""
Basic Flask application
with Babel integration for i18n.
"""

from flask import Flask, request, render_template
from flask_babel import Babel


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


@babel.localeselector
def get_locale():
    """
    Select the best match language
    for the user.
    """
    return request.accept_languages.best_match(app.config['LANGUGES'])


@app.route('/')
def index():
    """Render the index page."""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(debug=True)
