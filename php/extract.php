<?php

try {
    $phar = new Phar('aws.phar');
    $phar->extractTo('.\\aws'); // extract all files
 
} catch (Exception $e) {
    echo $e;
	
	
}

?>