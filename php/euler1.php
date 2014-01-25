<?php
$s = 0;
for($i = 0; $i < 10; $i++)
{
	if($i % 3 == 0){
		$s += $i;
			echo $i."\n";
	}
	else if($i % 5 == 0){
		$s += $i;
	echo $i."\n";
	}
}

echo $s."\n";

exit(0);

?>