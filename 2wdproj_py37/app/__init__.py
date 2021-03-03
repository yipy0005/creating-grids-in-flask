from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def hello():
    return redirect("/grid/overall")

from app.grid_map.views import gridmap as mod_gridmap

app.register_blueprint(mod_gridmap)
