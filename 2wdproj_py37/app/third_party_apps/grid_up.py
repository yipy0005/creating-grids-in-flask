# def grid_map(rows, cols, total_racks, rack_specific_details=0):
def grid_map(map_matrix, rack_specific_details=0):

    if rack_specific_details == 0:

        with open("app/templates/all_rack_coords.html", "w") as map_file:

            map_file.write(
                """
                <!DOCTYPE html>
                <html>
                <head>
                <title>General Map</title>
                """
            )

            # map_file.write(
            #     """
            #     <style>
            #     #overall_div {
            #         height: %ipx;
            #         width: %ipx;
            #         line-height: 0;
            #     }
            #     </style>
            #     """ % (50*cols, 50*rows)
            # )

            map_file.write(
                """
                </head>
                <body>

                <h1>General Map</h1>
                <br>
                <h3>Please edit the height and width of each rack to generate the largest possible warehouse area.</h3>
                <h3>Once done, click <a href="/grid/mapping" target="_blank">here</a> for the warehouse map.</h3>
                <br><br>
                <table>
                """
            )

            map_file.write(
                "{% for x in range("+str(rows)+") %}"
                "<tr>"
                "    {% for y in range("+str(cols)+") %}"
                "        {% for i in range(rack_no|length) %}"
                "            {% if rack_no[i]['rack_coords'][0] == x and rack_no[i]['rack_coords'][1] == y %}"
                """
                                <td>
                                    <a href="/grid/individual/{{ rack_no[i]['rack_id'] }}" target="_blank">{{ rack_no[i]['rack_id'] }}</a>
                                </td>
                            {% endif %}
                        {% endfor %}
                    {% endfor %}
                </tr>
                {% endfor %}
                """
            )

    elif rack_specific_details == 1:

        with open("app/templates/map.html", "w") as map_file:

            map_file.write(
                """
                <!DOCTYPE html>
                <html>
                <head>
                <script src="https://code.jquery.com/jquery-3.1.1.min.js" integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8=" crossorigin="anonymous"></script>
                <title>Actual Map</title>
                """
            )

            map_file.write(
                """
                <style>
                #main {
                    height: 750px;
                    width: 1000px;
                    line-height: 0;
                }

                table, th, td {
                    border: 1px solid black;
                    border-collapse: collapse;
                    text-align: center;
                }
                </style>
                """
            )

            map_file.write(
                """
                </head>
                <body>

                <h1>Actual Map</h1>
                <br><br>

                <script src="https://superal.github.io/canvas2image/canvas2image.js"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/0.4.1/html2canvas.min.js"></script>

                <button type="button" onclick="doCapture();">Save Map as PNG</button>
                <br><br>

                <div id="main">

                <img id="blank_grid" src="{{ url_for('static', filename='image1.png') }}" style="width:50px;height:50px;float:left;">
                <img id="blank_grid" src="{{ url_for('static', filename='image1.png') }}" style="width:50px;height:50px;float:left;">
                <img id="grid_A" src="{{ url_for('static', filename='alphabets/A.png') }}" style="width:50px;height:50px;float:left;">
                <img id="blank_grid" src="{{ url_for('static', filename='image1.png') }}" style="width:50px;height:50px;float:left;">
                <img id="grid_B" src="{{ url_for('static', filename='alphabets/B.png') }}" style="width:50px;height:50px;float:left;">
                <img id="grid_C" src="{{ url_for('static', filename='alphabets/C.png') }}" style="width:50px;height:50px;float:left;">
                <img id="blank_grid" src="{{ url_for('static', filename='image1.png') }}" style="width:50px;height:50px;float:left;">
                <img id="grid_D" src="{{ url_for('static', filename='alphabets/D.png') }}" style="width:50px;height:50px;float:left;">
                <img id="grid_E" src="{{ url_for('static', filename='alphabets/E.png') }}" style="width:50px;height:50px;float:left;">
                <img id="blank_grid" src="{{ url_for('static', filename='image1.png') }}" style="width:50px;height:50px;float:left;">
                <img id="grid_F" src="{{ url_for('static', filename='alphabets/F.png') }}" style="width:50px;height:50px;float:left;">
                <img id="grid_G" src="{{ url_for('static', filename='alphabets/G.png') }}" style="width:50px;height:50px;float:left;">
                <img id="blank_grid" src="{{ url_for('static', filename='image1.png') }}" style="width:50px;height:50px;float:left;">
                <img id="grid_H" src="{{ url_for('static', filename='alphabets/H.png') }}" style="width:50px;height:50px;float:left;">
                <img id="grid_I" src="{{ url_for('static', filename='alphabets/I.png') }}" style="width:50px;height:50px;float:left;">
                <img id="blank_grid" src="{{ url_for('static', filename='image1.png') }}" style="width:50px;height:50px;float:left;">
                <img id="grid_J" src="{{ url_for('static', filename='alphabets/J.png') }}" style="width:50px;height:50px;float:left;">
                <img id="grid_K" src="{{ url_for('static', filename='alphabets/K.png') }}" style="width:50px;height:50px;float:left;">
                <img id="blank_grid" src="{{ url_for('static', filename='image1.png') }}" style="width:50px;height:50px;float:left;">
                <img id="grid_L" src="{{ url_for('static', filename='alphabets/L.png') }}" style="width:50px;height:50px;float:left;">
                """
            )

            # for i in range(total_racks):
            #     map_file.write(
            #         """
            #         <img class="myButton" id="%i" src="{# {{ url_for('static', filename='image1.png') }} #}" style="width:50px;height:50px;float:left;">
            #         """ % i
            #     )

            map_file.write(
                """
                {% for i in range(map_matrix|length) %}
                    {% for each_col in map_matrix[i] %}
                        {% if each_col == 0 %}
                            <img id="{{ each_col }}_{{ i }}" src="{{ url_for('static', filename='image1.png') }}" style="width:50px;height:50px;float:left;">
                        {% elif each_col == 3 %}
                            <img id="{{ each_col }}_{{ i }}" src="{{ url_for('static', filename='Depot.png') }}" style="width:50px;height:50px;float:left;">
                        {% else %}
                            <img id="{{ each_col }}_{{ i }}" src="{{ url_for('static', filename='image2.png') }}" style="width:50px;height:50px;float:left;">
                        {% endif %}
                    {% endfor %}
                {% endfor %}
                """
            )

            map_file.write(
                """
                </div>
                <script>
                    document.querySelector('button').addEventListener('click', function() {
                        html2canvas(document.querySelector('#main'), {
                            onrendered: function(canvas) {
                            // document.body.appendChild(canvas);
                            return Canvas2Image.saveAsPNG(canvas);
                            }
                        });
                    });
                </script>
                </body>
                </html>
                """
            )

            map_file.write(
                """
                <script>
                    var myButton = document.getElementsByClassName("myButton");
                    var i;
                    for (i = 0; i < myButton.length; i++) {
                        var imgList = ["{{ url_for('static', filename='image1.png') }}","{{ url_for('static', filename='image2.png') }}", "{{ url_for('static', filename='image3.png') }}"];

                        var ButtonID = document.getElementsByClassName('myButton')[i].id
                        var myImage = document.getElementById(ButtonID)
                        myImage.onclick = function( e ){
                            var elem = e.target,
                            imageIndex = parseInt(elem.dataset.img,10);
                            if( imageIndex <= (imgList.length -1) ) {
                                elem.src = imgList[imageIndex++];
                                elem.dataset.img = imageIndex;
                            } else {
                                elem.src = imgList[0];
                                elem.dataset.img = 1;
                            }
                        }
                    }
                </script>
                </div>
                </body>
                </html>
                """
            )
