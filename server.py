
from flask import Flask
from flask import request
from buildall import build_simple
import os
app = Flask(__name__)

@app.route("/") # ‘https://www.google.com/‘
def home():
    return open('index.html')


@app.route("/templates")
def templates():
    type = request.args.get('type')
    id = request.args.get('id')
    build_simple()

    if id == 'all':
        return open(f"{type}_all.html")
    
    return open(f'{type}/{id}.html')
    