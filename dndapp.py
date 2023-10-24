from flask import Flask, render_template, url_for,request,redirect
from waitress import serve
import database as db
from werkzeug.security import generate_password_hash, check_password_hash

# Instanciando la APP

app = Flask(__name__)

# Config MYSQL


# Rutas

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/auth/login')
def login():
    return render_template('auth/login.html')

@app.route('/auth/register')
def register():
    return render_template('auth/register.html')

@app.route('/registro_usuario', methods=['POST'])
def newUser():
    email = request.form['email']
    usuario = request.form['usuario']
    password = generate_password_hash(request.form['password'], method="pbkdf2", salt_length=16)
    
    if email and usuario and password:
        cursor = db.database.cursor()
        sql = 'INSERT INTO usuarios (usuario_nombre, usuario_password, usuario_email) VALUES (%s, %s, %s)'
        data = (usuario, password, email)
        cursor.execute(sql,data)
        db.database.commit()
    return redirect(url_for('login'))

#if __name__ == "__main__":
#    serve(app, host="0.0.0.0", port=8000)