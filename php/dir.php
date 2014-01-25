<?php
echo $argv[1]."\n";
	function navigate_directory($path)
	{
		if ($handle = opendir($path)) {
			// echo "Directory handle: $handle\n";
			// echo "Entries:\n";

			/* This is the correct way to loop over the directory. */
			while (false !== ($entry = readdir($handle))) 
			{
				if(is_dir($path.'/'.$entry) && !preg_match("/[.]+/", $entry))
					navigate_directory($path.'/'.$entry);
				// echo "$entry\n";
				if(!is_dir($path.'/'.$entry) && preg_match("/[a-zA-Z_\-.]+.html/", $entry))
				{
					$lines = "";
					$fc = fopen ($path.'/'.$entry, "r"); 
					//echo 'opening'.$path.'/'.$entry,"\n";
					while (!feof ($fc))  
					{ 
						$buffer = fgets($fc, 4096); 
						$lines .= $buffer; 
					} 
					//echo $buffer;
					echo preg_replace("/([a-zA-Z0-9.]+)@[a-zA-Z0-9.]+/","$1@*****", $lines)."\n";
					fclose ($fc);	 

				}
			}



			closedir($handle);
		}


	}
navigate_directory($argv[1]);
?>