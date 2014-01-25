<?php
$n = 2;

$primes = Array();

if( $n % 2 == 0)
{
	$primes[2] = 1;
}
for($i = 3; $i <= 10; $i += 2)
getPrimes($i);

function getPrimes($n)
{
	global $primes;
	if(isset($primes[$n]))
		return true;
	echo "getPrimes($n)\n";
	$sq = ceil(sqrt($n));
	$ret = true;
	if( $n % 2 == 0)
		$ret = false;
	for($i = 3; $i <= $sq; $i += 2)
	{
		
		if($n % $i == 0)
		{
			
			$ret = false;
			getPrimes($i);
			
		}

	}
	if($ret == true)
		$primes[$n] = 1;
	return $ret;
}
$sum = 0;
foreach($primes as $k=>$v)
{
	echo $k."\n";
	$sum += $k; 
}
	echo $sum;
?>