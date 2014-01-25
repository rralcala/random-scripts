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
$c=0;
$pos = Array();
foreach($receivers as $rkey=>$rvalue)	
{
	$nr =false;
	$c = 0;
	foreach($senders as $pkey=>$pvalue)	
	{

			if($rkey == $pkey)
			{
				$nr = true;
			}
		
	}
	if(!$nr)
	{
		$pos [$rkey] = 1; 
	}
	
}

$fp = fopen("transactions.csv","r+");$c=0;
$dups = 0;

while(!feof($fp))
{
	$line = fgets($fp);
	list ($from, $to, $balance) = explode(",",$line);
	$from = trim($from);
	$to = trim($to);
	$balance = trim( $balance);
	if(isset($pos[$to]))
		echo $line;

}
fclose($fp);
/*
$c=0;
$roots = Array();
foreach($tree as $rkey=>$rvalue)	
{
	$nr =false;
	$c = 0;
	foreach($tree as $pkey=>$pvalue)	
	{
		foreach($pvalue as $ckey=>$cvalue)
		{
			if($rkey == $ckey)
			{
				$nr = true;
			}
		}
	}
	if(!$nr)
	{
		$roots [$rkey] = 1; 
	}
	
}*/
//echo $c;
//echo count($tree);
$loops = 0;
$moneyAtLeafs = 0;
//echo "<map version=\"0.9.0\"><node  TEXT=\"Epin FLow\">";
/*
foreach($roots as $key=>$value)
{
	$ret = Array();
	print_child($key, $tree, "", $ret);
	foreach($ret as $rk=>$rv)
		echo $key.",".$rk."\n";
}*/
	//echo "</node></map>";
//echo "Loops=".$loops."\n";
//echo"moneyAtLeafs=".$moneyAtLeafs."\n";



?>