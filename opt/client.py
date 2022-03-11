from opt.protobuf import hello_pb2

req = hello_pb2.HelloRequest()
req.name = "bbbb"
reqStr = req.SerializeToString()
print(reqStr)
