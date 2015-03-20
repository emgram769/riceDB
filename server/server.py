from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
import time
import random
import threading

hostName = "0.0.0.0"
hostPort = 9000
staticPort = 9001

class MyServer(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header("Content-type", "application/json")
    self.end_headers()
    #self.path
    out = """[
{
  "Name": "%s repo",
  "Program": "i3",
  "Description": "This is a sample of the description field.",
  "URL": "http://bwasti.com:9001/test.zip",
  "Images": ["http://bwasti.com:9001/test.jpg"]
},
{
  "Name": "%s repo 2",
  "Program": "i3",
  "Description": "Does this description thing work?.",
  "URL": "http://bwasti.com:9001/test.zip",
  "Images": ["http://bwasti.com:9001/test2.jpg"]
},
{
  "Name": "%s repo 3",
  "Program": "i3",
  "Description": "test.",
  "URL": "http://bwasti.com:9001/test.zip",
  "Images": ["http://bwasti.com:9001/test3.png"]
}
]""" % (self.path[1:], self.path[1:], self.path[1:])
    self.wfile.write(bytes(out, "utf-8"))

queryServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

def staticServer(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = (hostName, staticPort)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

s = threading.Thread(target=staticServer)
s.setDaemon(True)
s.start()

try:
  queryServer.serve_forever()
except KeyboardInterrupt:
  pass

queryServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
