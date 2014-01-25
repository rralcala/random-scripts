<?php
	if(isset($argv[1]))
	$handle = fopen($argv[1],"r+");
	else
		exit(0);
	
	$str = "";
	
	while(!feof($handle))
		$str .= fgets($handle);
	// Replaces a group of whitespaces with only one.
	$str = preg_replace("/\s+/"," ",$str);
	fclose($handle);
	$handle = fopen($argv[1],"w");
	fwrite($handle, $str);
	fclose($handle);
	
	
	
?>