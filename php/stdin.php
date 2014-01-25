#!/usr/bin/php
<?php
function connectToService($address, $service_port)
{
	/* Create a TCP/IP socket. */
	$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
	if ($socket === false) {
	    postReport($address,2,"socket_create() failed: reason: " . socket_strerror(socket_last_error()));
	} 

	echo "Attempting to connect to '$address' on port '$service_port'...";
	$result = socket_connect($socket, $address, $service_port);
	if ($result === false) {
		postReport($address,1,"socket_connect() failed.\nReason: ($result)");//. socket_strerror(socket_last_error($socket))
	}
	else
	{
		$out = socket_read($socket, 128);
		preg_match("/SSH\-[0-9]\.[0-9]\-OpenSSH_([0-9]\.[0-9])/",$out,$sshMatch);
		echo "OpenSSH Version = ".$sshMatch[1]."\n";
		socket_close($socket);
	}
}

$stdin = fopen('php://stdin', 'r');
while(!feof($stdin))
{
	$read[] =  fgets($stdin);
	
}
echo "recibido el eof.\n";
foreach($read as $host)
{
		$ipaddr = "";
  	
		if(preg_match("/[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/",$host,$match))
		{
			if($match[0] != ($rhost = gethostbyaddr($match[0])))
				echo $rhost."\n";
			else
				postReport($match[0],0," no tiene reverso"); 
			$ipaddr = $match[0];
		}
		else
		{	if(preg_match("/([a-z\-]+)(\.[0-9a-z\-]+)*/",$host,$match))
			if($match[0] != ($ipaddr = gethostbyname($match[0])))
				echo gethostbyaddr($ipaddr)."\n";
			else{
				postReport($match[0],0," no tiene reverso");
				$ipaddr = "";
			}
		}
	if($ipaddr != "")
		connectToService($ipaddr,22);
}

function postReport($host,$errCode,$errString)
{
$fields_string = "";
	//set POST variables
	$url = 'http://localhost/netTicket.php';
	$fields = array(
		    'host'=>urlencode($host),
		    'errCode'=>urlencode($errCode),
		    'errString'=>urlencode($errString),
		);

	//url-ify the data for the POST
	foreach($fields as $key=>$value) { $fields_string .= $key.'='.$value.'&'; }
	rtrim($fields_string,'&');
 
	//open connection
	$ch = curl_init();

	//set the url, number of POST vars, POST data
	curl_setopt($ch,CURLOPT_URL,$url);
	curl_setopt($ch,CURLOPT_POST,count($fields));
	curl_setopt($ch,CURLOPT_POSTFIELDS,$fields_string);
	curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
	curl_setopt($ch,CURLOPT_HEADER,0);
	
	//execute post
	$result = curl_exec($ch);
	echo "POST Says:".$result."\n";
	//close connection
	curl_close($ch);
}


print_r($read);
fclose($stdin);
?>
