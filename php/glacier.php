<?php
  $data = array("Date" => '2013-01-12', "Authorization" => 'vPwerCzUC0v5aCKjePKcX8N8Zw6bntfFSiMyrMfT', "x-amz-glacier-version" => "2012-06-01");
        $ch = curl_init('http://glacier.us-east-1.amazonaws.com' . '/6067-7486-2986/vaults/VaultName');
 
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "PUT");
        curl_setopt($ch, CURLOPT_POSTFIELDS,http_build_query($data));
 
        $response = curl_exec($ch);
        if(!$response) {
            return false;
        }
?>6067-7486-2986