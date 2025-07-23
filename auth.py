from flask import Blueprint, render_template,request, flash, redirect, url_for, session
from werkzeug.security import check_password_hash, generate_password_hash
from auth import auth
import pymysql
from functools import wraps

auth = Blueprint("auth", __name__)

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'example',
    'database': "auth_db",
    "port": 3306,
    "charset": "utf8mb4"
}

def get_db():
    return pymysql.connect(**DB_CONFIG)

def init_db():
    """테이블 생성"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            name VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.sign_in'))
        return f(*args, **kwargs)
    return decorated


@auth.route('/sign-in', methods=['GET', 'POST']) # login
def sign_in():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, password FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            session['user_name'] = user[1]
            return redirect(url_for('views.index'))
        flash("로그인 실패")

    return '''
    <form method="post">
        <input type="email" name="email" placeholder="이메일" required><br>
        <input type="password" name="password" placeholder="패스워드" required><br>
        <button type="submit">로그인</button>
    </form>
    <a href="/sign-up">회원가입</a>
    '''

@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.sign_in'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        password = request.form['password']
        
        conn = get_db()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (email, name, password) VALUES (%s, %s, %s)",
                (email, name, generate_password_hash(password))
            )
            conn.commit()
            flash('회원가입 완료')
            return redirect(url_for('auth.sign_in'))
        except pymysql.IntegrityError:
            flash('이미 존재하는 이메일')
        finally:
            conn.close()
    
    return '''
    <form method="post">
        <input type="email" name="email" placeholder="이메일" required><br>
        <input type="text" name="name" placeholder="이름" required><br>
        <input type="password" name="password" placeholder="패스워드" required><br>
        <button type="submit">회원가입</button>
    </form>
    <a href="/sign-in">로그인</a>
    '''