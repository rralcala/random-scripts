<?php
$greatest = 0;
for($i = 999; $i > 100; $i--)
for($j = 999; $j > 100; $j--)
	if((strrev($i*$j) == ($i*$j)) && ($i*$j) > $greatest){
		$greatest = $i*$j;
		//break 2;
	}
	
	echo $greatest."\n";
exit(0);

?>