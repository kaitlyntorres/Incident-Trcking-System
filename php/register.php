<?php
$conn=mysqli_connect('localhost', 'root', '','users') or die("Unable to connect :( ");

// referenced from w3schools.com

$firstname=$_POST['firstname'];
$lastname=$_POST['lastname'];
$username=$_POST['username'];
$password=$_POST['password'];


$sql="INSERT INTO 'regUser'('firstname', 'lastname', 'username', 'password' )VALUES('$name', '$lastname', '$username','$password')";
$result=mysql_query($conn,$sql);

if($result){
  echo "Successful";
  echo "<BR>";
  echo "<a href='signin.html'>Lets Login</a>";
  }
  else {
  echo "ERROR";
  }
  // close connection
  mysql_close();
  ?>
