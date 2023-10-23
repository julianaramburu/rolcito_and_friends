from flask import Flask, render_template

app = Flask(__name__)

# Rutas

@app.route('/')
def hello():
    render_template('index.html')