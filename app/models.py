from flask_sqlalchemy import SQLAlchemy

# Initialize the database object
db = SQLAlchemy()

# Define a User table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each user
    name = db.Column(db.String(80), nullable=False)  # Name of the user
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email of the user

    def __repr__(self):
        return f'<User {self.name}>'
