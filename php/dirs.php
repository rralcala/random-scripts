#!/usr/bin/php
<?php
function readpath($path)
{
	if ($handle = opendir($path)) {
	    //echo "Directory handle: $handle\n";
	    echo "Entries:\n";

	    /* This is the correct way to loop over the directory. */
	    while (false !== ($entry = readdir($handle))) {
		
		if(is_file($path."/".$entry))
		{
			echo $path."/".$entry."\t".filesize($path."/".$entry)."\n";	
		}		
		else 
		{
			echo $path."/".$entry."\n";		
			if($entry!="." && $entry!="..")
				readpath($path."/".$entry);
		}
		
	    }


	    closedir($handle);
	}
}

readpath($argv[1]);
?>

