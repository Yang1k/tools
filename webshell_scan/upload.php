<?php
session_start();
$_SESSION['filename'] = $_FILES["file"]["name"];
$_SESSION['time'] = time();
$name = end(explode('.',$_FILES['file']['name']));
if ($name != 'zip') {
    echo  "<script language=\"JavaScript\"> alert('目前只支持zip格式的文件!');window.history.back(-1); </script> ";
}else{
    move_uploaded_file($_FILES["file"]["tmp_name"],"upload/" . $_FILES["file"]["name"]);
}
       
?>
