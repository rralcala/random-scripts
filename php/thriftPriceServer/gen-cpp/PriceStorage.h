/**
 * Autogenerated by Thrift Compiler (0.9.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#ifndef PriceStorage_H
#define PriceStorage_H

#include <thrift/TDispatchProcessor.h>
#include "price_types.h"

namespace tutorial {

class PriceStorageIf {
 public:
  virtual ~PriceStorageIf() {}
  virtual void ping() = 0;
  virtual int32_t setItem(const Item& newItem) = 0;
  virtual void getItem(Item& _return, const int32_t itemId) = 0;
  virtual void zip() = 0;
};

class PriceStorageIfFactory {
 public:
  typedef PriceStorageIf Handler;

  virtual ~PriceStorageIfFactory() {}

  virtual PriceStorageIf* getHandler(const ::apache::thrift::TConnectionInfo& connInfo) = 0;
  virtual void releaseHandler(PriceStorageIf* /* handler */) = 0;
};

class PriceStorageIfSingletonFactory : virtual public PriceStorageIfFactory {
 public:
  PriceStorageIfSingletonFactory(const boost::shared_ptr<PriceStorageIf>& iface) : iface_(iface) {}
  virtual ~PriceStorageIfSingletonFactory() {}

  virtual PriceStorageIf* getHandler(const ::apache::thrift::TConnectionInfo&) {
    return iface_.get();
  }
  virtual void releaseHandler(PriceStorageIf* /* handler */) {}

 protected:
  boost::shared_ptr<PriceStorageIf> iface_;
};

class PriceStorageNull : virtual public PriceStorageIf {
 public:
  virtual ~PriceStorageNull() {}
  void ping() {
    return;
  }
  int32_t setItem(const Item& /* newItem */) {
    int32_t _return = 0;
    return _return;
  }
  void getItem(Item& /* _return */, const int32_t /* itemId */) {
    return;
  }
  void zip() {
    return;
  }
};


class PriceStorage_ping_args {
 public:

  PriceStorage_ping_args() {
  }

  virtual ~PriceStorage_ping_args() throw() {}


  bool operator == (const PriceStorage_ping_args & /* rhs */) const
  {
    return true;
  }
  bool operator != (const PriceStorage_ping_args &rhs) const {
    return !(*this == rhs);
  }

  bool operator < (const PriceStorage_ping_args & ) const;

  uint32_t read(::apache::thrift::protocol::TProtocol* iprot);
  uint32_t write(::apache::thrift::protocol::TProtocol* oprot) const;

};


class PriceStorage_ping_pargs {
 public:


  virtual ~PriceStorage_ping_pargs() throw() {}


  uint32_t write(::apache::thrift::protocol::TProtocol* oprot) const;

};


class PriceStorage_ping_result {
 public:

  PriceStorage_ping_result() {
  }

  virtual ~PriceStorage_ping_result() throw() {}


  bool operator == (const PriceStorage_ping_result & /* rhs */) const
  {
    return true;
  }
  bool operator != (const PriceStorage_ping_result &rhs) const {
    return !(*this == rhs);
  }

  bool operator < (const PriceStorage_ping_result & ) const;

  uint32_t read(::apache::thrift::protocol::TProtocol* iprot);
  uint32_t write(::apache::thrift::protocol::TProtocol* oprot) const;

};


class PriceStorage_ping_presult {
 public:


  virtual ~PriceStorage_ping_presult() throw() {}


  uint32_t read(::apache::thrift::protocol::TProtocol* iprot);

};

typedef struct _PriceStorage_setItem_args__isset {
  _PriceStorage_setItem_args__isset() : newItem(false) {}
  bool newItem;
} _PriceStorage_setItem_args__isset;

class PriceStorage_setItem_args {
 public:

  PriceStorage_setItem_args() {
  }

  virtual ~PriceStorage_setItem_args() throw() {}

  Item newItem;

  _PriceStorage_setItem_args__isset __isset;

  void __set_newItem(const Item& val) {
    newItem = val;
  }

  bool operator == (const PriceStorage_setItem_args & rhs) const
  {
    if (!(newItem == rhs.newItem))
      return false;
    return true;
  }
  bool operator != (const PriceStorage_setItem_args &rhs) const {
    return !(*this == rhs);
  }

  bool operator < (const PriceStorage_setItem_args & ) const;

  uint32_t read(::apache::thrift::protocol::TProtocol* iprot);
  uint32_t write(::apache::thrift::protocol::TProtocol* oprot) const;

};


class PriceStorage_setItem_pargs {
 public:


  virtual ~PriceStorage_setItem_pargs() throw() {}

  const Item* newItem;

  uint32_t write(::apache::thrift::protocol::TProtocol* oprot) const;

};

typedef struct _PriceStorage_setItem_result__isset {
  _PriceStorage_setItem_result__isset() : success(false), ouch(false) {}
  bool success;
  bool ouch;
} _PriceStorage_setItem_result__isset;

class PriceStorage_setItem_result {
 public:

  PriceStorage_setItem_result() : success(0) {
  }

  virtual ~PriceStorage_setItem_result() throw() {}

  int32_t success;
  InvalidOperation ouch;

  _PriceStorage_setItem_result__isset __isset;

  void __set_success(const int32_t val) {
    success = val;
  }

  void __set_ouch(const InvalidOperation& val) {
    ouch = val;
  }

  bool operator == (const PriceStorage_setItem_result & rhs) const
  {
    if (!(success == rhs.success))
      return false;
    if (!(ouch == rhs.ouch))
      return false;
    return true;
  }
  bool operator != (const PriceStorage_setItem_result &rhs) const {
    return !(*this == rhs);
  }

  bool operator < (const PriceStorage_setItem_result & ) const;

  uint32_t read(::apache::thrift::protocol::TProtocol* iprot);
  uint32_t write(::apache::thrift::protocol::TProtocol* oprot) const;

};

typedef struct _PriceStorage_setItem_presult__isset {
  _PriceStorage_setItem_presult__isset() : success(false), ouch(false) {}
  bool success;
  bool ouch;
} _PriceStorage_setItem_presult__isset;

class PriceStorage_setItem_presult {
 public:


  virtual ~PriceStorage_setItem_presult() throw() {}

  int32_t* success;
  InvalidOperation ouch;

  _PriceStorage_setItem_presult__isset __isset;

  uint32_t read(::apache::thrift::protocol::TProtocol* iprot);

};

typedef struct _PriceStorage_getItem_args__isset {
  _PriceStorage_getItem_args__isset() : itemId(false) {}
  bool itemId;
} _PriceStorage_getItem_args__isset;

class PriceStorage_getItem_args {
 public:

  PriceStorage_getItem_args() : itemId(0) {
  }

  virtual ~PriceStorage_getItem_args() throw() {}

  int32_t itemId;

  _PriceStorage_getItem_args__isset __isset;

  void __set_itemId(const int32_t val) {
    itemId = val;
  }

  bool operator == (const PriceStorage_getItem_args & rhs) const
  {
    if (!(itemId == rhs.itemId))
      return false;
    return true;
  }
  bool operator != (const PriceStorage_getItem_args &rhs) const {
    return !(*this == rhs);
  }

  bool operator < (const PriceStorage_getItem_args & ) const;

  uint32_t read(::apache::thrift::protocol::TProtocol* iprot);
  uint32_t write(::apache::thrift::protocol::TProtocol* oprot) const;

};


class PriceStorage_getItem_pargs {
 public:


  virtual ~PriceStorage_getItem_pargs() throw() {}

  const int32_t* itemId;

  uint32_t write(::apache::thrift::protocol::TProtocol* oprot) const;

};

typedef struct _PriceStorage_getItem_result__isset {
  _PriceStorage_getItem_result__isset() : success(false) {}
  bool success;
} _PriceStorage_getItem_result__isset;

class PriceStorage_getItem_result {
 public:

  PriceStorage_getItem_result() {
  }

  virtual ~PriceStorage_getItem_result() throw() {}

  Item success;

  _PriceStorage_getItem_result__isset __isset;

  void __set_success(const Item& val) {
    success = val;
  }

  bool operator == (const PriceStorage_getItem_result & rhs) const
  {
    if (!(success == rhs.success))
      return false;
    return true;
  }
  bool operator != (const PriceStorage_getItem_result &rhs) const {
    return !(*this == rhs);
  }

  bool operator < (const PriceStorage_getItem_result & ) const;

  uint32_t read(::apache::thrift::protocol::TProtocol* iprot);
  uint32_t write(::apache::thrift::protocol::TProtocol* oprot) const;

};

typedef struct _PriceStorage_getItem_presult__isset {
  _PriceStorage_getItem_presult__isset() : success(false) {}
  bool success;
} _PriceStorage_getItem_presult__isset;

class PriceStorage_getItem_presult {
 public:


  virtual ~PriceStorage_getItem_presult() throw() {}

  Item* success;

  _PriceStorage_getItem_presult__isset __isset;

  uint32_t read(::apache::thrift::protocol::TProtocol* iprot);

};


class PriceStorage_zip_args {
 public:

  PriceStorage_zip_args() {
  }

  virtual ~PriceStorage_zip_args() throw() {}


  bool operator == (const PriceStorage_zip_args & /* rhs */) const
  {
    return true;
  }
  bool operator != (const PriceStorage_zip_args &rhs) const {
    return !(*this == rhs);
  }

  bool operator < (const PriceStorage_zip_args & ) const;

  uint32_t read(::apache::thrift::protocol::TProtocol* iprot);
  uint32_t write(::apache::thrift::protocol::TProtocol* oprot) const;

};


class PriceStorage_zip_pargs {
 public:


  virtual ~PriceStorage_zip_pargs() throw() {}


  uint32_t write(::apache::thrift::protocol::TProtocol* oprot) const;

};

class PriceStorageClient : virtual public PriceStorageIf {
 public:
  PriceStorageClient(boost::shared_ptr< ::apache::thrift::protocol::TProtocol> prot) :
    piprot_(prot),
    poprot_(prot) {
    iprot_ = prot.get();
    oprot_ = prot.get();
  }
  PriceStorageClient(boost::shared_ptr< ::apache::thrift::protocol::TProtocol> iprot, boost::shared_ptr< ::apache::thrift::protocol::TProtocol> oprot) :
    piprot_(iprot),
    poprot_(oprot) {
    iprot_ = iprot.get();
    oprot_ = oprot.get();
  }
  boost::shared_ptr< ::apache::thrift::protocol::TProtocol> getInputProtocol() {
    return piprot_;
  }
  boost::shared_ptr< ::apache::thrift::protocol::TProtocol> getOutputProtocol() {
    return poprot_;
  }
  void ping();
  void send_ping();
  void recv_ping();
  int32_t setItem(const Item& newItem);
  void send_setItem(const Item& newItem);
  int32_t recv_setItem();
  void getItem(Item& _return, const int32_t itemId);
  void send_getItem(const int32_t itemId);
  void recv_getItem(Item& _return);
  void zip();
  void send_zip();
 protected:
  boost::shared_ptr< ::apache::thrift::protocol::TProtocol> piprot_;
  boost::shared_ptr< ::apache::thrift::protocol::TProtocol> poprot_;
  ::apache::thrift::protocol::TProtocol* iprot_;
  ::apache::thrift::protocol::TProtocol* oprot_;
};

class PriceStorageProcessor : public ::apache::thrift::TDispatchProcessor {
 protected:
  boost::shared_ptr<PriceStorageIf> iface_;
  virtual bool dispatchCall(::apache::thrift::protocol::TProtocol* iprot, ::apache::thrift::protocol::TProtocol* oprot, const std::string& fname, int32_t seqid, void* callContext);
 private:
  typedef  void (PriceStorageProcessor::*ProcessFunction)(int32_t, ::apache::thrift::protocol::TProtocol*, ::apache::thrift::protocol::TProtocol*, void*);
  typedef std::map<std::string, ProcessFunction> ProcessMap;
  ProcessMap processMap_;
  void process_ping(int32_t seqid, ::apache::thrift::protocol::TProtocol* iprot, ::apache::thrift::protocol::TProtocol* oprot, void* callContext);
  void process_setItem(int32_t seqid, ::apache::thrift::protocol::TProtocol* iprot, ::apache::thrift::protocol::TProtocol* oprot, void* callContext);
  void process_getItem(int32_t seqid, ::apache::thrift::protocol::TProtocol* iprot, ::apache::thrift::protocol::TProtocol* oprot, void* callContext);
  void process_zip(int32_t seqid, ::apache::thrift::protocol::TProtocol* iprot, ::apache::thrift::protocol::TProtocol* oprot, void* callContext);
 public:
  PriceStorageProcessor(boost::shared_ptr<PriceStorageIf> iface) :
    iface_(iface) {
    processMap_["ping"] = &PriceStorageProcessor::process_ping;
    processMap_["setItem"] = &PriceStorageProcessor::process_setItem;
    processMap_["getItem"] = &PriceStorageProcessor::process_getItem;
    processMap_["zip"] = &PriceStorageProcessor::process_zip;
  }

  virtual ~PriceStorageProcessor() {}
};

class PriceStorageProcessorFactory : public ::apache::thrift::TProcessorFactory {
 public:
  PriceStorageProcessorFactory(const ::boost::shared_ptr< PriceStorageIfFactory >& handlerFactory) :
      handlerFactory_(handlerFactory) {}

  ::boost::shared_ptr< ::apache::thrift::TProcessor > getProcessor(const ::apache::thrift::TConnectionInfo& connInfo);

 protected:
  ::boost::shared_ptr< PriceStorageIfFactory > handlerFactory_;
};

class PriceStorageMultiface : virtual public PriceStorageIf {
 public:
  PriceStorageMultiface(std::vector<boost::shared_ptr<PriceStorageIf> >& ifaces) : ifaces_(ifaces) {
  }
  virtual ~PriceStorageMultiface() {}
 protected:
  std::vector<boost::shared_ptr<PriceStorageIf> > ifaces_;
  PriceStorageMultiface() {}
  void add(boost::shared_ptr<PriceStorageIf> iface) {
    ifaces_.push_back(iface);
  }
 public:
  void ping() {
    size_t sz = ifaces_.size();
    size_t i = 0;
    for (; i < (sz - 1); ++i) {
      ifaces_[i]->ping();
    }
    ifaces_[i]->ping();
  }

  int32_t setItem(const Item& newItem) {
    size_t sz = ifaces_.size();
    size_t i = 0;
    for (; i < (sz - 1); ++i) {
      ifaces_[i]->setItem(newItem);
    }
    return ifaces_[i]->setItem(newItem);
  }

  void getItem(Item& _return, const int32_t itemId) {
    size_t sz = ifaces_.size();
    size_t i = 0;
    for (; i < (sz - 1); ++i) {
      ifaces_[i]->getItem(_return, itemId);
    }
    ifaces_[i]->getItem(_return, itemId);
    return;
  }

  void zip() {
    size_t sz = ifaces_.size();
    size_t i = 0;
    for (; i < (sz - 1); ++i) {
      ifaces_[i]->zip();
    }
    ifaces_[i]->zip();
  }

};

} // namespace

#endif
