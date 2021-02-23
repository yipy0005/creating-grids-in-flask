from wtforms import Form, IntegerField

class GridParameters(Form):
    grid_length = IntegerField('Grid Length')
    grid_width = IntegerField('Grid Width')

class ObstacleGridParameters(Form):
    obstacle_grid_length = IntegerField('Obstacle Grid Length')
    obstacle_grid_width = IntegerField('Obstacle Grid Width')