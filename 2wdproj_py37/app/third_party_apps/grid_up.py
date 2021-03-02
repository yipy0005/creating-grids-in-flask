def grid_map(rows, cols, total_racks, rack_specific_details=0):

    if rack_specific_details == 0:

        with open("app/templates/all_rack_coords.html", "w") as map_file:

            # all_alphabets = [
            #     'A', 'B', 'C', 'D', 'E', 'F', 'G',
            #     'H', 'I', 'J', 'K', 'L', 'M', 'N',
            #     'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            #     'V', 'W', 'X', 'Y', 'Z'
            # ]
            # all_numbers = [i for i in range(26)]

            # alphabets = []
            # numbers = []
            # for i in range(length):
            #     numbers.append(all_numbers[i])
            # for i in range(width):
            #     alphabets.append(all_alphabets[i])

            # coordinate_system = []
            # for alphabet in alphabets:
            #     for number in numbers:
            #         coordinate_system.append(alphabet + str(number))

            # print(coordinate_system)

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

    # else:
    #     with open("app/templates/all_rack_coords.html", "w") as map_file:
    #         map_file.write('')

    elif rack_specific_details == 1:

        with open("app/templates/map.html", "w") as map_file:

            map_file.write(
                """
                <!DOCTYPE html>
                <html>
                <head>
                <title>Actual Map</title>
                """
            )

            map_file.write(
                """
                <style>
                #main {
                    height: %ipx;
                    width: %ipx;
                    line-height: 0;
                }
                </style>
                """ % (50*rows, 50*cols)
            )

            map_file.write(
                """
                </head>
                <body>

                <h1>Actual Map</h1>
                <br><br>
                <div id="main">
                """
            )

            map_file.write(
                """
                {% for coord in all_possible_coordinates %}
                    {% if coord in racks_coords %}
                        <img src="{{ url_for('static', filename='image2.png') }}" style="width:50px;height:50px;float:left;">
                    {% else %}
                        <img src="{{ url_for('static', filename='image1.png') }}" style="width:50px;height:50px;float:left;">
                    {% endif %}
                {% endfor %}
                """
            )

            map_file.write(
                """
                </div>
                </body>
                </html>
                """
            )

        # # 1D Matrix
        # for coordinates in coordinate_system:
        #     map_file.write(
        #         """
        #         <img class="myButton" id="%s" src="{# {{ url_for('static', filename='image1.png') }} #}" style="width:50px;height:50px;float:left;">
        #         """ % coordinates
        #     )

        # map_file.write(
        #     """
        #     <script>
        #         var myButton = document.getElementsByClassName("myButton");
        #         var i;
        #         for (i = 0; i < myButton.length; i++) {
        #             var imgList = ["{# {{ url_for('static', filename='image1.png') }} #}","{# {{ url_for('static', filename='image2.png') }} #}", "{# {{ url_for('static', filename='image3.png') }} #}"];

        #             var ButtonID = document.getElementsByClassName('myButton')[i].id
        #             var myImage = document.getElementById(ButtonID)
        #             myImage.onclick = function( e ){
        #                 var elem = e.target,
        #                 imageIndex = parseInt(elem.dataset.img,10);
        #                 if( imageIndex <= (imgList.length -1) ) {
        #                     elem.src = imgList[imageIndex++];
        #                     elem.dataset.img = imageIndex;
        #                 } else {
        #                     elem.src = imgList[0];
        #                     elem.dataset.img = 1;
        #                 }
        #             }
        #         }
        #     </script>
        #     </div>
        #     </body>
        #     </html>
        #     """
        # )
