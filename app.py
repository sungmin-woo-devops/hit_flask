import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
from map import create_map
from views import views
from auth import auth

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://root:example@localhost:5432/postgres'

    db = SQLAlchemy(app)
    
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
