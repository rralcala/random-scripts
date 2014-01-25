<?php
$fp = fopen("names.txt","r+");

$str = fgets($fp);

fclose($fp);

$array = explode(",",$str);
for($i = 0; $i < count($array); $i++)
{
	$array[$i] = trim($array[$i], "\""); 
}
sort($array);
//print_r($array);
print_r($array);
$sum =  0;
foreach($array as $k=>$name)
{
	if($name == "COLIN")
		echo $k;
	$score= 0;
	for($i = 0; $i < strlen($name); $i++)
	{
		$score += (ord($name[$i])  - ord('A') + 1);
	
	}
		
		$score *= $k+1;
		$sum += $score;
	

}
echo $sum;
?>