<nav>
<ul class="horizontal">
  <li><a class="active" href="#ver">Vertical</a></li>
  <li><a href="tabulka.php">Tabulka</a></li>
   <?php 
  if (!isset($_SESSION["email"])){ 
    echo "<li><a href='register.php'>Register</a></li>
      <li><a href='login.php'>Login</a></li>";
    }
  if (isset($_SESSION["email"])) {
    echo "  <li style=' float:right ;'><a href='logout.php'> Logout</a></li>
    <li style='float:Right;'><div style='color: white;padding-top: 10px;'>Vítejte uživateli: {$_SESSION['email']}</div ></li>  ";
    }
  ?>
</ul>
</nav>