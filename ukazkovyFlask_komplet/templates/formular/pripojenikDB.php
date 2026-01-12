<?php
$servername = "dbs.spskladno.cz";
$username = "student14";
$password = "spsnet";
$dbname = "vyuka14";
$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
