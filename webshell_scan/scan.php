
<?php

session_start();
$filename =  $_SESSION['filename'];
$_SESSION['project'] = explode($filename,'.');
$a = system("python3 ./scan/scan.py $filename");
$url = "./#contact";
header("Location: $url");
?>