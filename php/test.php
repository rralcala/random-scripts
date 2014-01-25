<?php
require_once("lib.php");

$fp = fopen("ToStay.csv","r+");$c=0;
$dups = 0;

while(!feof($fp))
{
	$line = fgets($fp);
	list ($child, $forget, $parent, $balance, $lastTx) = explode(",",$line);
	if(trim($child) == trim($parent))
	{

		$roots[$child] = $balance;
	}
	if(!isset($tree[$parent]))
		$tree[$parent] = Array();
	$tree[$parent][$child] = $balance;
}
//echo "<map version=\"0.9.0\"><node  TEXT=\"New Mindmap\">";
foreach($roots as $key=>$value)
	print_child_simple($key, $tree);
//echo "</node></map>";
 
 
fclose($fp);


?>