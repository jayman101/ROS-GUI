import xmlrpclib

PORT = 8000
# Based on http://docs.python.org/library/xmlrpclib.html

proxy = xmlrpclib.ServerProxy("http://localhost:%s/" % PORT)

print("Connected. Calling TestFunction..")

response = proxy.TestFunction("The ships hung in the sky in much the same way that bricks don't.")
print("Server response: %s" % response)
print("Bye")
