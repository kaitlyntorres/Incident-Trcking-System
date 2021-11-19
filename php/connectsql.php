<?php>
$username=username
$password= "Sick1234"
// name of database
$db="users"
$conn= mysqli_connect("localhost",$username, $password, $db);

// referenced from w3schools.com
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
} 

?>
