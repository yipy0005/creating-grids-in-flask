<?php

$image = $_POST["image"];
$image = explode(";", $image)[1];

echo $image;
