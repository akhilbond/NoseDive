<html>
<head>
	<h1>
		"HELLOOO"
	</h1>
</head>
<body>
		<?php
		session_start();
		$uploaddir = "images/";
		$uploadfile = $uploaddir.basename($_FILES['userfile']['name']);


		if (move_uploaded_file($_FILES['userfile']['tmp_name'], $uploadfile)) {
		  echo "File is valid, and was successfully uploaded.\n";
		} else {
		   echo "Upload failed";
		}

		echo 'Here is some more debugging info:';
		print_r($_FILES);

		?>
</body>
</html> 