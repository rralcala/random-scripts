<?php
require_once("lib.php");

if(($fp = @fopen($argv[1],"r+")) === FALSE)
{
	echo "Error opening file ".$argv[1]."\n";
	exit(0);
}
$c=0;
$dups = 0;
$c = 0;
//$lineArray[23] Created Date
//$lineArray[23] Stock
//$lineArray[0] HP
//$lineArray[91] Last TX
//
while(!feof($fp))
{
	$line = fgets($fp);
	$lineArray = explode("|",$line);
	echo $lineArray[0].",".$lineArray[24].",".substr($lineArray[91],0,8)."\n";
	$sum += $lineArray[24];
}

fclose($fp);

?>