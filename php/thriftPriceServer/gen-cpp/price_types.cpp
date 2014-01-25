/**
 * Autogenerated by Thrift Compiler (0.9.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#include "price_types.h"

#include <algorithm>

namespace tutorial {

const char* Item::ascii_fingerprint = "0655A6BBC993E275D502CB0742593539";
const uint8_t Item::binary_fingerprint[16] = {0x06,0x55,0xA6,0xBB,0xC9,0x93,0xE2,0x75,0xD5,0x02,0xCB,0x07,0x42,0x59,0x35,0x39};

uint32_t Item::read(::apache::thrift::protocol::TProtocol* iprot) {

  uint32_t xfer = 0;
  std::string fname;
  ::apache::thrift::protocol::TType ftype;
  int16_t fid;

  xfer += iprot->readStructBegin(fname);

  using ::apache::thrift::protocol::TProtocolException;


  while (true)
  {
    xfer += iprot->readFieldBegin(fname, ftype, fid);
    if (ftype == ::apache::thrift::protocol::T_STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
        if (ftype == ::apache::thrift::protocol::T_I32) {
          xfer += iprot->readI32(this->id);
          this->__isset.id = true;
        } else {
          xfer += iprot->skip(ftype);
        }
        break;
      case 2:
        if (ftype == ::apache::thrift::protocol::T_STRING) {
          xfer += iprot->readString(this->name);
          this->__isset.name = true;
        } else {
          xfer += iprot->skip(ftype);
        }
        break;
      case 3:
        if (ftype == ::apache::thrift::protocol::T_STRING) {
          xfer += iprot->readString(this->barcode);
          this->__isset.barcode = true;
        } else {
          xfer += iprot->skip(ftype);
        }
        break;
      case 4:
        if (ftype == ::apache::thrift::protocol::T_DOUBLE) {
          xfer += iprot->readDouble(this->price);
          this->__isset.price = true;
        } else {
          xfer += iprot->skip(ftype);
        }
        break;
      default:
        xfer += iprot->skip(ftype);
        break;
    }
    xfer += iprot->readFieldEnd();
  }

  xfer += iprot->readStructEnd();

  return xfer;
}

uint32_t Item::write(::apache::thrift::protocol::TProtocol* oprot) const {
  uint32_t xfer = 0;
  xfer += oprot->writeStructBegin("Item");

  xfer += oprot->writeFieldBegin("id", ::apache::thrift::protocol::T_I32, 1);
  xfer += oprot->writeI32(this->id);
  xfer += oprot->writeFieldEnd();

  xfer += oprot->writeFieldBegin("name", ::apache::thrift::protocol::T_STRING, 2);
  xfer += oprot->writeString(this->name);
  xfer += oprot->writeFieldEnd();

  xfer += oprot->writeFieldBegin("barcode", ::apache::thrift::protocol::T_STRING, 3);
  xfer += oprot->writeString(this->barcode);
  xfer += oprot->writeFieldEnd();

  xfer += oprot->writeFieldBegin("price", ::apache::thrift::protocol::T_DOUBLE, 4);
  xfer += oprot->writeDouble(this->price);
  xfer += oprot->writeFieldEnd();

  xfer += oprot->writeFieldStop();
  xfer += oprot->writeStructEnd();
  return xfer;
}

void swap(Item &a, Item &b) {
  using ::std::swap;
  swap(a.id, b.id);
  swap(a.name, b.name);
  swap(a.barcode, b.barcode);
  swap(a.price, b.price);
  swap(a.__isset, b.__isset);
}

const char* InvalidOperation::ascii_fingerprint = "3F5FC93B338687BC7235B1AB103F47B3";
const uint8_t InvalidOperation::binary_fingerprint[16] = {0x3F,0x5F,0xC9,0x3B,0x33,0x86,0x87,0xBC,0x72,0x35,0xB1,0xAB,0x10,0x3F,0x47,0xB3};

uint32_t InvalidOperation::read(::apache::thrift::protocol::TProtocol* iprot) {

  uint32_t xfer = 0;
  std::string fname;
  ::apache::thrift::protocol::TType ftype;
  int16_t fid;

  xfer += iprot->readStructBegin(fname);

  using ::apache::thrift::protocol::TProtocolException;


  while (true)
  {
    xfer += iprot->readFieldBegin(fname, ftype, fid);
    if (ftype == ::apache::thrift::protocol::T_STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
        if (ftype == ::apache::thrift::protocol::T_I32) {
          xfer += iprot->readI32(this->what);
          this->__isset.what = true;
        } else {
          xfer += iprot->skip(ftype);
        }
        break;
      case 2:
        if (ftype == ::apache::thrift::protocol::T_STRING) {
          xfer += iprot->readString(this->why);
          this->__isset.why = true;
        } else {
          xfer += iprot->skip(ftype);
        }
        break;
      default:
        xfer += iprot->skip(ftype);
        break;
    }
    xfer += iprot->readFieldEnd();
  }

  xfer += iprot->readStructEnd();

  return xfer;
}

uint32_t InvalidOperation::write(::apache::thrift::protocol::TProtocol* oprot) const {
  uint32_t xfer = 0;
  xfer += oprot->writeStructBegin("InvalidOperation");

  xfer += oprot->writeFieldBegin("what", ::apache::thrift::protocol::T_I32, 1);
  xfer += oprot->writeI32(this->what);
  xfer += oprot->writeFieldEnd();

  xfer += oprot->writeFieldBegin("why", ::apache::thrift::protocol::T_STRING, 2);
  xfer += oprot->writeString(this->why);
  xfer += oprot->writeFieldEnd();

  xfer += oprot->writeFieldStop();
  xfer += oprot->writeStructEnd();
  return xfer;
}

void swap(InvalidOperation &a, InvalidOperation &b) {
  using ::std::swap;
  swap(a.what, b.what);
  swap(a.why, b.why);
  swap(a.__isset, b.__isset);
}

} // namespace
