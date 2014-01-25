<?php

foreach(glob('*',GLOB_ONLYDIR) as $file)
	echo $file.fileperms($file)."\n";

?>