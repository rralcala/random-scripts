#!/usr/bin/env php
<?php

namespace tutorial\php;

error_reporting(E_ALL);

require_once '/root/thrift-0.9.0/lib/php/lib/Thrift/ClassLoader/ThriftClassLoader.php';

use Thrift\ClassLoader\ThriftClassLoader;

$GEN_DIR = realpath(dirname(__FILE__)); 
echo $GEN_DIR;

$loader = new ThriftClassLoader();
$loader->registerNamespace('Thrift', '/root/thrift-0.9.0/lib/php/lib');
//$loader->registerDefinition('shared', $GEN_DIR);
$loader->registerDefinition('tutorial', $GEN_DIR);
$loader->register();

//require_once "tutorial/PriceStorage.php";
/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements. See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership. The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License. You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied. See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

use Thrift\Protocol\TBinaryProtocol;
use Thrift\Transport\TSocket;
use Thrift\Transport\THttpClient;
use Thrift\Transport\TBufferedTransport;
use Thrift\Exception\TException;

try {
  if (array_search('--http', $argv)) {
    $socket = new THttpClient('localhost', 8080, '/php/PhpServer.php');
  } else {
    $socket = new TSocket('localhost', 9090);
  }
  $transport = new TBufferedTransport($socket, 1024, 1024);
  $protocol = new TBinaryProtocol($transport);
  $client = new \tutorial\PriceStorageClient($protocol);

  $transport->open();

  $client->ping();
  print "ping()\n";

  $item = new \tutorial\Item();
  $item->id = 2;
  $item->name = 'Mayonesa';
  $item->barcode = '0120338924';
  $item->price = 12.4;
  
  $sum = $client->setItem($item);
//  print "1+1=$sum\n";

  //$work = new \tutorial\Work();

 // $work->op = \tutorial\Operation::DIVIDE;
 // $work->num1 = 1;
 // $work->num2 = 0;

  try {

    $item = $client->getItem( 2);
    print $item->barcode."\n";
  } catch (\tutorial\InvalidOperation $io) {
    print "InvalidOperation: $io->why\n";
  }
/*
  $work->op = \tutorial\Operation::SUBTRACT;
  $work->num1 = 15;
  $work->num2 = 10;
  $diff = $client->calculate(1, $work);
  print "15-10=$diff\n";

  $log = $client->getStruct(1);
  print "Log: $log->value\n";

  $transport->close();
*/
} catch (TException $tx) {
  print 'TException: '.$tx->getMessage()."\n";
}

?>