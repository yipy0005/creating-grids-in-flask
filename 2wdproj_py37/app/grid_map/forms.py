from wtforms import Form, IntegerField


class OverallRackParams(Form):
    total_no_of_racks = IntegerField('Total No. of Racks')
    no_of_racks_per_row = IntegerField('No. of Racks Per Row')
    no_of_racks_per_col = IntegerField('No. of Racks Per Column')


class IndividualRackParams(Form):
    rack_height = IntegerField('Rack Height')
    rack_width = IntegerField('Rack Width')
    # grid_length = IntegerField('Grid Length')
    # grid_width = IntegerField('Grid Width')

# class ObstacleGridParameters(Form):
#     obstacle_grid_length = IntegerField('Obstacle Grid Length')
#     obstacle_grid_width = IntegerField('Obstacle Grid Width')