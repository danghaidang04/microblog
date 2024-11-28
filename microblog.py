# When we type 'flask run' in the terminal, it will look for a Flask application instance
# in the module referenced by the FLASK_APP environment variable,
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}
