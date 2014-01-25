<?php
function largestPrime($number)
{
	echo (ceil($number / 2) - 1)."\n";
	for($i = (ceil($number / 2)-1); $i > 0; $i-=2)
	{
		if($number % $i == 0)
			return $i;
			
	}
	return 0;

}

//
 
echo largestPrime(600851475143)."\n";

exit(0);

?>