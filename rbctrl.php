<!DOCTYPE html>
<html>
<head>
    <title> ROBOT: Smart Factory Control System</title>
    <meta charset="UTF-8">
    <meta name="viewpoint" content="width=30", initial-scale=1.0">
</head>
<body>
    <h2>ROBOT is moving. . .  &gt;&gt;</h2>
    
    <form method="post" action="robotctrl.php">
        <input type="submit" value="MOVING" name="moving">
        <input type="submit" value="BACK" name="back">
    </form>
    <br><br><br>
    <hr>
    
    <?php
    $servername = "localhost";
	$user = "root";
	$password = "0000";
	$dbname = "ConveyorBelt"; 
	
	if(isset($_POST['back'])){
	$conn = new mysqli($servername, $user, $password, $dbname);
	
    if ($conn->connect_error) {
        echo "<h2>Connecting to the Server is FAIL</h2>";
    } else {
        echo "<h2>Connecting to the Server is Successful</h2>";
        
        echo "<h3 align=center> - - ROBOT res- - </h3>";

        // <table> table form:default
        $sql4 = "SELECT * FROM Robot"; // Robot table
        $result4 = $conn->query($sql4);

        if (isset($result4) && $result4->num_rows > 0) {
            echo "<table border='3' align=center>";
            echo "<tr><th>robotID</th><th>robotNAME</th>
            <th>curLOC</th><th>rLINE</th>
            <th>rTIME</th></tr>";
            
            while ($row = $result4->fetch_assoc()) {
                // input to the table
                echo "<tr align=center>
                <td>". $row["robotID"]."</td>
                <td>". $row["robotNAME"]."</td>
                <td>".$row["curLOC"]."</td>
                <td>". $row["rLINE"]."</td>
                <td>".$row["rTIME"]."</td>
                </tr>";
            }
            echo "</table>";
        } else {
            echo "0 results";
        }
    }
}
	if(isset($_POST['moving'])){ //result : insert msg to socket  
		$conn = new mysqli($servername, $user, $password, $dbname);
            
        $sql5 = "SELECT * FROM rResult";
        $result5 = $conn->query($sql5);
            
        if (isset($result5)) {
            echo "<h3> Displayed data cleaned successfully.</h3>";
            {
				echo "<table border='3' align=center>";
				echo "<tr><th>finresultID</th><th>productID</th>
				<th>robotID</th><th>rLINE</th><th>curLOC</th>
				<th>rTIME</th></tr>";
            
				while ($row = $result5->fetch_assoc()) {
					// show the table
					echo "<tr align=center>
					<td>". $row["finresultID"]."</td>
					<td>". $row["productID"]."</td>
					<td>".$row["robotID"]."</td>
					<td>". $row["rLINE"]."</td>
					<td>". $row["curLOC"]."</td>
					<td>".$row["rTIME"]."</td>
					</tr>";
				}
				echo "</table>";
			}
        } else {
            echo "<h3> Cleaning data failed.</h3>";
        }
    }	
    ?>
</body>
</html>


===================================

<!DOCTYPE html>
<html>
<head>
    <title> ROBOT: Smart Factory Control System</title>
    <meta charset="UTF-8">
    <meta name="viewpoint" content="width=30", initial-scale=1.0">
</head>
<body>
    <h2>ROBOT is moving. . .  &gt;&gt;</h2>
    
    <form method="post" action="robotcytl.php">
        <input type="submit" value="MOVING" name="moving">
        <input type="submit" value="BACK" name="clean">
    </form>
    <br><br><br>
    <hr>
    
    <?php
    $servername = "localhost";
	$user = "root";
	$password = "0000";
	$dbname = "ConveyorBelt"; 
	
	if(isset($_POST['moving'])){
	$conn = new mysqli($servername, $user, $password, $dbname);
	
    if ($conn->connect_error) {
        echo "<h2>Connecting to the Server is FAIL</h2>";
    } else {
        echo "<h2>Connecting to the Server is Successful</h2>";
        
        echo "<h3 align=center> - - ROBOT res- - </h3>";

        // <table> table form:default
        $sql1 = "SELECT * FROM Robot"; // Product table
        $result1 = $conn->query($sql1);

        if (isset($result1) && $result1->num_rows > 0) {
            echo "<table border='3' align=center>";
            echo "<tr><th>robotID</th><th>robotNAME</th>
            <th>curLOC</th><th>rLINE</th>
            <th>rTIME</th></tr>";
            
            while ($row = $result1->fetch_assoc()) {
                // input to the table
                echo "<tr align=center>
                <td>". $row["robotID"]."</td>
                <td>". $row["robotNAME"]."</td>
                <td>".$row["curLOC"]."</td>
                <td>". $row["rLINE"]."</td>
                <td>".$row["rTIME"]."</td>
                </tr>";
            }
            echo "</table>";
        } else {
            echo "0 results";
        }
    }
}
	if(isset($_POST['clean'])){
		$conn = new mysqli($servername, $user, $password, $dbname);
            
        $sql3 = "UPDATE Robot SET curLOC = '', rLINE = '', rTIME = ''";
        $result3 = $conn->query($sql3);
            
        if ($result3) {
            echo "<h3> Displayed data cleaned successfully.</h3>";
        } else {
            echo "<h3> Cleaning data failed.</h3>";
        }
    }	
    ?>
</body>
</html>



============================

<!DOCTYPE html>
<html>
<head>
    <title> ROBOT: Smart Factory Control System</title>
    <meta charset="UTF-8">
    <meta name="viewpoint" content="width=30", initial-scale=1.0">
</head>
<body>
    <h2>ROBOT is moving. . .  &gt;&gt;</h2>
    
    <form method="post" action="robotcytl.php">
        <input type="submit" value="MOVING" name="moving">
        <input type="submit" value="BACK" name="clean">
    </form>
    <br><br><br>
    <hr>
    
    <?php
    $servername = "localhost";
	$user = "root";
	$password = "0000";
	$dbname = "ConveyorBelt"; 
	
	if(isset($_POST['moving'])){
	$conn = new mysqli($servername, $user, $password, $dbname);
	
    if ($conn->connect_error) {
        echo "<h2>Connecting to the Server is FAIL</h2>";
    } else {
        echo "<h2>Connecting to the Server is Successful</h2>";
        
        echo "<h3 align=center> - - ROBOT res- - </h3>";

        // <table> table form:default
        $sql1 = "SELECT * FROM Robot"; // Product table
        $result1 = $conn->query($sql1);

        if (isset($result1) && $result1->num_rows > 0) {
            echo "<table border='3' align=center>";
            echo "<tr><th>robotID</th><th>robotNAME</th>
            <th>curLOC</th><th>rLINE</th>
            <th>rTIME</th></tr>";
            
            while ($row = $result1->fetch_assoc()) {
                // input to the table
                echo "<tr align=center>
                <td>". $row["robotID"]."</td>
                <td>". $row["robotNAME"]."</td>
                <td>".$row["curLOC"]."</td>
                <td>". $row["rLINE"]."</td>
                <td>".$row["rTIME"]."</td>
                </tr>";
            }
            echo "</table>";
        } else {
            echo "0 results";
        }
    }
}
	if(isset($_POST['clean'])){
		$conn = new mysqli($servername, $user, $password, $dbname);
            
        $sql3="DELETE curLOC,rLINE,rTIME FROM Robot";
        $result3=$conn->query($sql3);
            
        if (isset($result3)) { //&& $result3->num_rows > 0
			echo "<table border='3' align=center>";
			echo "<tr><th>robotID</th><th>robotNAME</th>
				<th>curLOC</th><th>rLINE</th>
				<th>rTIME</th></tr>";
            
            while ($row = $result1->fetch_assoc()) {
                // input to the table
                echo "<tr align=center>
                <td>". $row["robotID"]."</td>
                <td>". $row["robotNAME"]."</td>
                <td>".$row["curLOC"]."</td>
                <td>". $row["rLINE"]."</td>
                <td>".$row["rTIME"]."</td>
                </tr>";
            }
				echo "</table>";
			} else{
				echo "<h3> Displayed data cleaned successfully.</h3>";
			}
				
        }	
    
    
    ?>
    
</body>
</html>
