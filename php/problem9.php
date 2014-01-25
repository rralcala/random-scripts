<?php
$c = 0;
for($i = 1; $i < 1000; $i++)
{
	for($j = 1; $j < $i; $j++)
	{
		for($k = 1; $k < $j; $k++)
		{
			//if( $i < $j && $j < $k)
			{
				if((($k*$k) + ($j*$j)) == $i*$i)
					if(($i+$j+$k) == 1000)
						echo ($i*$j*$k)."\n";
			}
		}
	}
//	echo $i."\n";
}
echo $c;
?>