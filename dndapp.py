from flask import Flask, render_template, url_for
from waitress import serve

app = Flask(__name__)

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

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)