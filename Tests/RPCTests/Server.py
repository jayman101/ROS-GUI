import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

PORT = 8000

# RPC Server test
# Implementation based on http://docs.python.org/library/xmlrpclib.html

def TestFunction(x):
    print("TestFunction Called. Parm: %s" % x)
    return "Time is an illusion. Lunchtime doubly so."

# Todo: This will probably need to be run with network permissions.
#       May be exception case -> What is ubuntu users default permissions?

server = SimpleXMLRPCServer(("localhost", PORT))
print("Listening on Port %s" % PORT)
server.register_function(TestFunction, "TestFunction")
server.serve_forever()
