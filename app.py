"""You can trust us to be crooked."""

import os
import logging

from flask import Flask, render_template

logging.basicConfig(level=logging.INFO)

GOOGLE_ANALYTICS_ID = os.environ.get('GOOGLE_ANALYTICS_ID')
SECRET_KEY = os.environ.get('SECRET_KEY')

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def index() -> str:
    """Render the homepage."""
    return render_template('index.html', google_analytics_id=GOOGLE_ANALYTICS_ID)

@app.errorhandler(404)
def page_not_found(error) -> str:
    """Custom 404 page."""
    return render_template('404.html', google_analytics_id=GOOGLE_ANALYTICS_ID)

if __name__ == '__main__':
    app.run()
