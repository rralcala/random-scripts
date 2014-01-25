<?php

$fp = fopen("tx.csv","r+");$c=0;
$dups = 0;

$receivers = Array();
$senders = Array();

while(!feof($fp))
{
	$line = fgets($fp);
	list ($from, $name, $to, $date, $balance) = explode(",",$line);
	$from = trim($from);
	$to = trim($to);
	if($date[0])
	if(!isset($senders[$from]))
		$senders[$from] = trim($balance);
	else
		$senders[$from] += trim($balance);
		
		
	if(!isset($receivers[$to]))
		$receivers[$to] = trim($balance);
	else
		$receivers[$to] += trim($balance);	
}
fclose($fp);
$sum = 0;
$count = 0;
foreach($senders as $skey=>$value)
{
	if(!isset($receivers[$skey]))
	{
		echo "$skey,$value\n";
		$sum += $value;
		if($value>0)
		$c++;
	}
}
echo number_format($sum). " " . $c."\n";

$sum = 0;
$count = 0;
foreach($receivers as $skey=>$value)
{
	if(!isset($senders[$skey]))
	{
//		echo "Receiver $skey $value \n";
		$sum += $value;
		if($value>0)
		$c++;
	}
}
echo number_format($sum). " " . $c."\n";


?>