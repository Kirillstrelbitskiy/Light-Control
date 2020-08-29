<?php
  $connection = mysqli_connect("own-server.zzz.com.ua","Kirill","My271320!Ps_21Qt","kirillstrelok_1");

  $id = $_GET['id'];
  $state = $_GET['state'];

  $query_to_update = "UPDATE sh_smart_home SET state=$state WHERE id=$id";
  $result = mysqli_query($connection, $query_to_update) or die(mysqli_error($connection));
?>
