<?php
$stream = popen("netstat -n");

// 

while(!feof($stream))
{
    $buffer = fgets($stream);
    preg_match(
    "/\s[a-z]+\s[0-9]+\s[0-9]+\s(?:[0-9]{1,3}+\.){4}:[0-9]+\s(?:[0-9]{1,3}+\.){4}:([0-9]+)\s(TIME_WAIT|ESTABLISHED)",$buffer,$result);
    
    
    if(isset($ports[$results[1]][$results[2]]))
    	$ports[$results[1]][$results[2]]++;
    else
        $ports[$results[1]][$results[2]] = 1;
        
}
foreach($ports as $k=>$port)
    echo "Port ".$k." - ESTABLISHED: ".$port['ESTABLISHED']." TIME_WAIT: ".$port['TIME_WAIT']."\n";
  
    fclose($stream);
?>