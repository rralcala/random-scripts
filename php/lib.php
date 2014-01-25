<?php

function print_child($root, &$tree, $path = "",&$ret)
{
global $moneyAtLeafs;
global $loops;
if(!isset($ret[$root]))
	$ret[$root] = 1;
//echo $path.($path!=""?",":"").$root."\n";
//echo "<node TEXT=\"$root\">";
//echo $root." in ".$path."  Result=".strpos($path, (string)$root)."\n";
	foreach($tree[$root] as $key=>$value)
	{
		
		if(isset($tree[$key])) 
		{
			if(!strpos($path, (string)$key))
				print_child($key, $tree, $path.($path!=""?",":"").$root, $ret);
			else
			{
				//$loops++;
				//echo $path.",".$root.",".$key." = ".$value."LOOP \n";//"<node TEXT=\"$key $valueLOOP\"/>";
			}
		}
		else 
		{
			//$moneyAtLeafs += $value;
			//echo $path.",".$root.",".$key."\n";
			//echo "<node TEXT=\"$key $value\"/>";
		}
		
	}
//echo "</node>";
}

function print_child_simple(&$root, &$tree)
{
echo "<node TEXT=\"$root\">";
	foreach($tree[$root] as $key=>$value)
	{
		//echo "Dealer: ".$key." Balance: ".$value."\n";
		if(isset($tree[$key]) && $key != $root)
			print_child($key, $tree);
		else
			echo "<node TEXT=\"$key\"/>";
	}
echo "</node>";
}
?>