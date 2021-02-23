from flask import Blueprint, render_template, request

from app.grid_map.forms import GridParameters, ObstacleGridParameters

from app.third_party_apps.grid_up import grid_obstacle

gridmap = Blueprint(
    'gridmap', __name__,
    url_prefix='/grid',
)

@gridmap.route('/', methods=['GET', 'POST'])
def gridding():
    overall_form = GridParameters(request.form)
    obstacle_form = ObstacleGridParameters(request.form)

    if request.method == 'POST' and overall_form.validate(): #or obstacle_form.validate():

        grid_obstacle(overall_form.grid_length.data, overall_form.grid_width.data)
        
        return render_template('map.html')
    
    return render_template('grid.html', overall_form=overall_form, obstacle_form=obstacle_form)