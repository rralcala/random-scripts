<?php

// Include the SDK using the Composer autoloader
require 'AWSSDKforPHP/aws.phar';

use Aws\Glacier\GlacierClient;
use Aws\Common\Enum\Region;

// Instantiate the DynamoDB client with your AWS credentials
$client = GlacierClient::factory(array(
  'key'    => 'AKIA',
  'secret' => 'private-key',
  'region' => Region::US_EAST_1
));
//echo 'AA'.$client->ssl_verification.'\n';
//$client->disable_ssl_verification();
/*$result = $client->uploadArchive(array(
  'vaultName' => 'phpVault',
  'body' => 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa',
  'archiveDescription' => 'Test',
  'ContentSHA256' => hash('sha256', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa'),
  'checksum' =>  hash('sha256', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa')

));*/

$result = $client->ListVaults(array(

 
));

var_dump($result);
// Wait until the table is created and active
//$client->waitUntil('TableExists', $table);

//echo "The {$table} table has been created.\n";
