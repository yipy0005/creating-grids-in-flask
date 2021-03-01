from flask import Blueprint, render_template, request, redirect

from app.grid_map.forms import OverallRackParams, IndividualRackParams

from app.third_party_apps.grid_up import grid_map
import json

gridmap = Blueprint(
    'gridmap', __name__,
    url_prefix='/grid',
)

@gridmap.route('/overall', methods=['GET', 'POST'])
def overall_racking():
    all_alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    form = OverallRackParams(request.form)

    if request.method == 'POST' and form.validate(): #or obstacle_form.validate():

        no_of_rows = int(form.total_no_of_racks.data / form.no_of_racks_per_row.data)
        no_of_cols = int(form.total_no_of_racks.data / form.no_of_racks_per_col.data)

        # all_alphabets = all_alphabets[0:no_of_cols]

        # all_rack_coords = []
        all_racks = []
        
        rack_data = {}
        rack_data['rack_info'] = []
        # for alphabet in all_alphabets:
        for i in range(no_of_rows*no_of_cols):
            # all_rack_coords.append(alphabet+str(i))
            all_racks.append('rack'+str(i))
            rack_data['rack_info'].append(
                {
                    'rack_id': 'rack'+str(i), #alphabet+str(i),
                    'height': 0,
                    'width': 0
                }
            )
        
        with open('racks_infos.txt', 'w') as outfile:
            json.dump(rack_data, outfile, indent=4)

        return render_template('all_rack_coords.html', all_racks=all_racks)
                    
    return render_template('overall_rack_form.html', form=form)


@gridmap.route('/individual/<rackid>', methods=['GET', 'POST'])
def individual_racking(rackid):
    form = IndividualRackParams(request.form)

    with open('racks_infos.txt', 'r') as json_file:
        rack = json.load(json_file)

    all_racks = []
    for each_rack in rack['rack_info']:
        all_racks.append(each_rack['rack_id'])

    for each_rack in rack['rack_info']:
        if each_rack['rack_id'] == rackid:
            rack_id = rackid
            if request.method == 'POST' and form.validate():
                each_rack['height'] = int(form.rack_height.data)
                each_rack['width'] = int(form.rack_width.data)
    
    with open('racks_infos.txt', 'w') as json_file:
        json.dump(rack, json_file, indent=4)
    
        return render_template('individual_rack_form.html', form=form, rack_id=rack_id)
    
    return render_template('all_rack_coords.html', all_racks=all_racks)


@gridmap.route('/mapping', methods=['GET', 'POST'])
def mapping():

    with open('racks_infos.txt', 'r') as json_file:
        rack = json.load(json_file)

    grid_map()

    return render_template('map.html')