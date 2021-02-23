from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

from app.grid_map.views import gridmap as mod_gridmap

app.register_blueprint(mod_gridmap)