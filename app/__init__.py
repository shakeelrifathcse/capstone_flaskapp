from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

def create_app():
    """Factory to create and configure the app."""
    app = Flask(__name__)

    # App configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app/database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    from app.routes import main
    app.register_blueprint(main)

    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    return app
