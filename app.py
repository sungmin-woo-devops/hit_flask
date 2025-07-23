from flask import Flask, render_template, request, flask, redirect, url_for, session
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
from map import create_map
import os


def create_app(**kwargs):
    """Creates a new Flask app using the Factory Pattern"""
    app = Flask(__name__)
    app.config.update(kwargs)
    
    # 메인 페이지 라우트 추가
    from views import views
    from auth import auth
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
