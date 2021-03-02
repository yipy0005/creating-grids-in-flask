from flask import Blueprint, render_template, request

from app.grid_map.forms import OverallRackParams, IndividualRackParams

from app.third_party_apps.grid_up import grid_map
import json

gridmap = Blueprint(
    'gridmap', __name__,
    url_prefix='/grid',
)

@gridmap.route('/overall', methods=['GET', 'POST'])
def overall_racking():
    # all_alphabets = [
    #     'A', 'B', 'C', 'D', 'E', 'F', 'G',
    #     'H', 'I', 'J', 'K', 'L', 'M', 'N',
    #     'O', 'P', 'Q', 'R', 'S', 'T', 'U',
    #     'V', 'W', 'X', 'Y', 'Z'
    # ]

    form = OverallRackParams(request.form)

    if request.method == 'POST' and form.validate():
        no_of_rows = int(
            form.total_no_of_racks.data / form.no_of_racks_per_row.data
        )
        no_of_cols = int(
            form.total_no_of_racks.data / form.no_of_racks_per_col.data
        )

        all_rack_coords = []
        for y in range(no_of_cols):
            for x in range(no_of_rows):
                all_rack_coords.append((x, y))

        # all_alphabets = all_alphabets[0:no_of_cols]

        # all_rack_coords = []
        # all_racks = []

        rack_data = {}
        rack_data['rack_info'] = []
        # for alphabet in all_alphabets:
        for i in range(no_of_rows*no_of_cols):
            # all_rack_coords.append(alphabet+str(i))
            # all_racks.append('rack'+str(i))
            rack_data['rack_info'].append(
                {
                    'rack_id': 'rack'+str(i), #alphabet+str(i),
                    'rack_coords': all_rack_coords[i],
                    'height': 0,
                    'width': 0
                }
            )

        with open('racks_infos.txt', 'w') as outfile:
            json.dump(rack_data, outfile, indent=4)

        grid_map(
            no_of_rows,
            no_of_cols,
            no_of_rows*no_of_cols,
            0
        )

        return render_template(
            'all_rack_coords.html',
            # all_racks=all_racks,
            rack_no=rack_data['rack_info'],
            no_of_rows=no_of_rows,
            no_of_cols=no_of_cols
        )

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

        return render_template(
            'individual_rack_form.html',
            form=form,
            rack_id=rack_id
        )

    return render_template('all_rack_coords.html', all_racks=all_racks)


@gridmap.route('/mapping', methods=['GET', 'POST'])
def mapping():

    with open('racks_infos.txt', 'r') as json_file:
        rack = json.load(json_file)

    total_required_rows = []
    total_racks_in_a_row = []
    total_required_cols = []
    total_racks_in_a_col = []

    for each_rack in rack['rack_info']:
        total_racks_in_a_row.append(each_rack['rack_coords'][0])
        total_racks_in_a_col.append(each_rack['rack_coords'][1])

    total_racks_in_a_row = len(set(total_racks_in_a_row))
    total_racks_in_a_col = len(set(total_racks_in_a_col))

    for x in range(total_racks_in_a_row):
        required_rows = []
        for each_rack in rack['rack_info']:
            if each_rack['rack_coords'][0] == x:
                required_rows.append(each_rack['height'])
        total_required_rows.append(max(required_rows))
    
    for y in range(total_racks_in_a_col):
        required_cols = []
        for each_rack in rack['rack_info']:
            if each_rack['rack_coords'][1] == y:
                required_cols.append(each_rack['width'])
        total_required_cols.append(max(required_cols))

    total_required_rows = sum(total_required_rows) + total_racks_in_a_row + 1
    total_required_cols = sum(total_required_cols) + total_racks_in_a_col + 1

    all_possible_coordinates = []
    for x in range(total_required_rows):
        for y in range(total_required_cols):
            all_possible_coordinates.append([x, y])

    racks_coords = []
    for each_rack in rack['rack_info']:
        each_rack_coords = [each_rack['width'], each_rack['height']]

    grid_map(
        total_required_rows,
        total_required_cols,
        total_racks_in_a_row*total_racks_in_a_col,
        1
    )

    return render_template(
        'map.html',
        all_possible_coordinates=all_possible_coordinates,
        racks_coords=racks_coords
    )
