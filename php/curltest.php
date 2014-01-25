#!/usr/bin/php
<?php
        // create curl resource 
        $ch = curl_init(); 

        // set url 
        curl_setopt($ch, CURLOPT_URL, "www.kernel.org"); 

        //return the transfer as a string 
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); 

        // $output contains the output string 
        $output = curl_exec($ch); 

        // close curl resource to free up system resources 
        curl_close($ch);    
preg_match_all("/<td >(mainline:|stable:)<\/td>[^<]*<td ><strong>([0-9]+\.[0-9]+(?:[.-][0-9a-z-.]+)?)<\/strong><\/td>/s",$output, $matches,PREG_SET_ORDER);
foreach($matches as $match)
{
	echo $match[1].$match[2]."\n";
}

?>

