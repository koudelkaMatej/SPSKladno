<?php
include 'pripojenikDB.php';
session_start();
?>
<?php

    if ($_SERVER["REQUEST_METHOD"] == "POST" || $_SERVER["REQUEST_METHOD"] == "GET") {

        $sql_create = "CREATE TABLE IF NOT EXISTS users0 (
        id INT PRIMARY KEY AUTO_INCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
        )";

        $result = $conn->query($sql_create);
        if ($result === TRUE) {
            echo "Tabulka vytvořena.";
        } else {
            echo "Tabulku se nepodařilo vytvořit. Chyba: " . $conn->error;
        }

        $conn->close();

        $username = $_POST['jmeno'];
        $email = $_POST['email'];
        $password = md5($_POST['psw']);
        $sql_insert = "INSERT INTO users0(username, email, password) VALUES ('$username','$email','$password')";
        $result = $conn->query($sql_insert);
        if ($result === TRUE) {
            echo "Uživatel byl úspěšně registrován";
        } else {
            echo "Registrace se nezdařila" . $conn->error;
        }
    }
      $conn->close();
      header("location: login.php");
    ?>
