<?php
function fibonacci($element)
{

	$s = 1;
	$s2 = 1;
	for($i = 0; $i <= $element; $i++)
	{
		$sum = $s + $s2;
		$s = $s2;
		$s2 = $sum;
		
	}
	return $sum;

}
$sum = 0;
for($i = 0; ($value = fibonacci($i)) < 4000000; $i++)
{
echo $value."\n";
	if($value % 2 == 0){
		$sum += $value;
		
	}
}

echo $sum."\n";

exit(0);

?>