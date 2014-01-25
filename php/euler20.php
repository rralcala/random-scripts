<?php


function factorial($n)
{
	if($n == 0) 
		return 1;
	else 
		return gmp_mul($n,factorial($n-1));

}

	
	$str = gmp_strval(factorial(100)); 
	$sum = 0; 
	//echo $str."\n";
for($i = 0; $i < strlen($str) ; $i++)
{
	$sum += $str[$i];
	echo $str[$i];
}
	echo "\n".number_format($sum,0,"","")."\n";
exit(0);

?>
