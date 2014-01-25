<?php
$sumSq = 0;
$sqSum = 0;
for($i = 1; $i <= 100; $i++)
{
 $sumSq += $i*$i;
 $sqSum += $i; 

}
echo ($sqSum*$sqSum) - $sumSq;
?>