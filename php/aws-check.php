<?php

// Include the SDK using the Composer autoloader
require 'AWSSDKforPHP/aws.phar';

use Aws\DynamoDb\DynamoDbClient;
use Aws\Common\Enum\Region;

// Instantiate the DynamoDB client with your AWS credentials
$client = DynamoDbClient::factory(array(
  'key'    => 'AKIAILUTYWDOMB5GG5WQ',
  'secret' => 'f3rNjfWCjqA0GdWblbjWOd1GY9X8F+/oYUc6JltJ',
  'region' => Region::US_EAST_1
));
//echo 'AA'.$client->ssl_verification.'\n';
//$client->disable_ssl_verification();

$table = 'posts';
// Create a "posts" table
$result = $client->createTable(array(
  'TableName' => $table,
  'KeySchema' => array(
      'HashKeyElement' => array(
          'AttributeName' => 'slug',
          'AttributeType' => 'S'
      )
  ),
  'ProvisionedThroughput' => array(
      'ReadCapacityUnits'  => 10,
      'WriteCapacityUnits' => 5
  )
));

// Wait until the table is created and active
$client->waitUntil('TableExists', $table);

echo "The {$table} table has been created.\n";
