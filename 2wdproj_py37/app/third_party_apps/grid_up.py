def grid_map(length, width):
    with open("app/templates/map.html", "w") as map_file:

        all_alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        all_numbers = [i for i in range(26)]

        alphabets = []
        numbers = []
        for i in range(length):
            numbers.append(all_numbers[i])
        for i in range(width):
            alphabets.append(all_alphabets[i])
        
        coordinate_system = []
        for alphabet in alphabets:
            for number in numbers:
                coordinate_system.append(alphabet + str(number))
        
        print(coordinate_system)
            

        map_file.write(
            """
            <!DOCTYPE html>
            <html>
            <head>
            <title>Map</title>
            <style>
            """
        )
                
        map_file.write(
            """
            #main {
                height: %ipx;
                width: %ipx;
                line-height: 0;
            }
            """ % (50*length, 50*width)
        )

        map_file.write(
            """
            </style>
            </head>
            <body>

            <h1>Grid Map</h1>
            <br><br>
            <div id="main">
            """
        )

        # 1D Matrix
        for coordinates in coordinate_system:
            map_file.write(
                """
                <img class="myButton" id="%s" src="{{ url_for('static', filename='image1.png') }}" style="width:50px;height:50px;float:left;">
                """ % coordinates
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