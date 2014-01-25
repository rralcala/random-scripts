<?php 
  if(($stream = popen("ps ax","r")) === FALSE)
  {
  	echo "ERR";
  	exit(0);
}
//echo $stream."\n";
 stream_set_blocking($stream, 0);
 $data = "";
 $matches = Array();
 while(!feof($stream))
 {
 	$data .= fgets($stream);
 	
 }
 echo preg_match_all( "/^\s*([0-9]+)\s+[a-z0-9\/?]+\s+([a-zR<+]+)/m" , $data , $matches, PREG_SET_ORDER);
//echo $data;
foreach($matches as $match)
echo $match[1]."\t".$match[2]."\n";
 //print_r($matches);
 fclose($stream);