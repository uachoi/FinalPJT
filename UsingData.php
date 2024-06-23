<!DOCTYPE html>
<html>
<head><title> Smart Factory Control System </title></head>
<body>
	<h2> Object Identification Results >> </h2>
	
	<form method="get" action="dbresults.php">
		<input type="submit" value="SEARCH" name="search">
		<input type="submit" value="CLEAN" name="clean">
		<input type="submit" value="RELOAD" name="reload">
		
	</form>
	<?php
		//Connecting to the Server//
		$servername="localhost:3306";
		$user="root";
		$password="0000";
		$dbname="ConveyorBelt"; //ConveyorBelt: Product, cResult, Transmission
		
		$conn=new mysqli($servername, $user, $password, $dbname); //Connecting test
		if($conn->connect_error){
			echo "<h2> Connecting to the Server is FAIL </h2>";
		}
		else echo "<h2> Connecting to the Server is Susccessful </h2>";

		$sql1="SELECT*FROM Product"; // Product table
		$result1=$conn->query($sql1);
		
		if($result1->num_rows > 0){
			//$row=$result1->fetch_assoc()
			while($row=$result1->fetch_assoc()){
				echo "productID: " . $row["productID"] . " - productCOLOR: " . $row["productCOLOR"] .
            " - productSIZE: " . $row["productSIZE"] . " - productLOCATION: " . $row["productLOCATION"] .
            " - productTS: " . $row["productTS"] . " - robotID: " . $row["robotID"] . " - pTIME: " . $row["pTIME"] . "<br>";
			}
		else{
			echo "0 results"; }
		}
		$conn->close();
	?>
	
</body>
</html>
