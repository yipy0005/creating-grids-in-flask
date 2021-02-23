from flask import Flask, request, render_template
from forms import GridParameters
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/grid', methods=['GET', 'POST'])
def gridding():
    form = GridParameters(request.form)

    if request.method == 'POST' and form.validate():
        print(form.grid_length.data)
        print(form.grid_width.data)
    
    return render_template('grid.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)