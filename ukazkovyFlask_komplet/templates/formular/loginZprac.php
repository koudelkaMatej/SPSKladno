<?php
session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $servername = "dbs.spskladno.cz";
  $username = "student14";
  $password = "spsnet";
  $dbname = "vyuka14";

  $conn = new mysqli($servername, $username, $password, $dbname);

  // Check for successful connection
  if ($conn->connect_error) {
      die("Connection failed: " . $conn->connect_error);
  }

  $username = $_POST["jmeno"];
  $password = $_POST["psw"]; //připsat md5 pokud použito

  $sql = "SELECT username, password, email FROM users0 WHERE username = '$username' AND password = '$password'";
  $result = $conn->query($sql);

 if ($result->num_rows > 0) {
    // Start the session
    $zaznam = $result->fetch_assoc();
    $_SESSION["loggedin"] = true;
    $_SESSION["username"] = $username;
    $_SESSION["email"] = $zaznam["email"];
}
$conn->close();
}
    header("location: tabulka.php");
?>

 
