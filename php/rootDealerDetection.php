<?php
require_once("lib.php");

$fp = fopen("transactions.csv","r+");$c=0;
$dups = 0;

while(!feof($fp))
{
	$line = fgets($fp);
	list ($from, $to, $balance) = explode(",",$line);
	$from = trim($from);
	$to = trim($to);
	$balance = trim( $balance);
	$senders[$from] = 1;
	$receivers[$to] = 1;

		if(!isset($tree[$from]))
			$tree[$from] = Array();
		if(!isset($tree[$from][$to]))
			$tree[$from][$to] = $balance;
		else
			$tree[$from][$to] += $balance;

}
fclose($fp);



foreach($roots as $key=>$value)
{
	print_child_simple($key, $tree);
}
	//echo "</node></map>";
 
 


?>