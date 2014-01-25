// This autogenerated skeleton file illustrates how to build a server.
// You should copy it to another filename to avoid overwriting it.

#include "PriceStorage.h"
#include <thrift/protocol/TBinaryProtocol.h>
#include <thrift/server/TSimpleServer.h>
#include <thrift/transport/TServerSocket.h>
#include <thrift/transport/TBufferTransports.h>
#include <string.h>
#include <iostream>
#include <map>
#include <utility>
#include <hiredis/hiredis.h>

using namespace ::apache::thrift;
using namespace ::apache::thrift::protocol;
using namespace ::apache::thrift::transport;
using namespace ::apache::thrift::server;

using boost::shared_ptr;

using namespace  ::tutorial;
using namespace std;

class PriceStorageHandler : virtual public PriceStorageIf {
 private:
	map<int32_t,Item*> Items;
	 redisContext *c;
    redisReply *reply;
	
 public:
  PriceStorageHandler() {
    

    struct timeval timeout = { 1, 500000 }; // 1.5 seconds
    c = redisConnectWithTimeout((char*)"127.0.0.1", 6379, timeout);
    if (c->err) {
        printf("Connection error: %s\n", c->errstr);
        exit(1);
    }

    /* PING server */
    reply = (redisReply *)redisCommand(c,"PING");
    printf("PING: %s\n", reply->str);
    freeReplyObject(reply);
  }

  void ping() {
    // Your implementation goes here
    printf("ping\n");
  }

  int32_t setItem(const Item& newItem) {
    if(Items.find(newItem.id) == Items.end())
	{
		reply = (redisReply *)redisCommand(c,"SET items:%d:name %s", newItem.id, newItem.name.c_str());
		printf("SET: %s\n", reply->str);
		freeReplyObject(reply);
		reply = (redisReply *)redisCommand(c,"SET items:%d:barcode %s", newItem.id, newItem.barcode.c_str());
		printf("SET: %s\n", reply->str);
		freeReplyObject(reply);
		reply = (redisReply *)redisCommand(c,"SET items:%d:price %f", newItem.id, newItem.price);
		printf("SET: %s\n", reply->str);
		freeReplyObject(reply);
		
		cout << newItem.id << endl;
	}
	return 0;
  }

  void getItem(Item& _return, const int32_t itemId) {
	cout << "Requested" << itemId << endl;
	reply = (redisReply *)redisCommand(c,"GET items:%d:name", itemId);
    printf("GET foo: %s\n", reply->str);
    
    if(reply->str == NULL)
	{
		freeReplyObject(reply);
		InvalidOperation io;
        io.what = itemId;
        io.why = "Cannot find it";
        throw io;
	}
	else
	{
		
		_return.id = itemId;
		/* Try a GET and two INCR */
    _return.name =  std::string (reply->str);
	
	freeReplyObject(reply);
	
	 reply = (redisReply *)redisCommand(c,"GET items:%d:barcode", itemId);
    printf("GET foo: %s\n", reply->str);
	_return.barcode =  std::string (reply->str);
    freeReplyObject(reply);
		//_return.barcode = reply->str;
		
		_return.price = 0.0;
		
	}
  }

  void zip() {
    // Your implementation goes here
    printf("zip\n");
  }

};

int main(int argc, char **argv) {
  int port = 9090;
  shared_ptr<PriceStorageHandler> handler(new PriceStorageHandler());
  shared_ptr<TProcessor> processor(new PriceStorageProcessor(handler));
  shared_ptr<TServerTransport> serverTransport(new TServerSocket(port));
  shared_ptr<TTransportFactory> transportFactory(new TBufferedTransportFactory());
  shared_ptr<TProtocolFactory> protocolFactory(new TBinaryProtocolFactory());

  TSimpleServer server(processor, serverTransport, transportFactory, protocolFactory);
  server.serve();
  return 0;
}

