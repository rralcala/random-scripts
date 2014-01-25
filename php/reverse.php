<?php


function reverse(&$array, $c = 0)
{
	$el1 = $array[$c];
	$el2 = $array[strlen($array) - 1 - $c];
	if(floor(strlen($array) / 2) > $c)
	{
		reverse($array, $c+1);
				
	}
	$array[$c] = $el2;
	$array[strlen($array) - 1 - $c] = $el1;
	
}

$str = 'hola que tal';
echo $str."\n";
reverse($str);
echo $str."\n";

?>