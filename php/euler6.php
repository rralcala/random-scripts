<?php
$greatest = 0;
for($i = 20; ; $i++){
	for($j = 1; $j < 21; $j++)
		if($i % $j != 0){
			break;
		}
		if($j == 21)
		{
			echo $i."\n";
			break;
		}
	
	}
//	echo $greatest."\n";
exit(0);

?>