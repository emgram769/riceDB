from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import random

hostName = "localhost"
hostPort = 9000

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
  "URL": "http://localhost:8000/test.zip",
  "Images": ["http://localhost:8000/test.jpg"]
},
{
  "Name": "%s repo 2",
  "Program": "i3",
  "Description": "Does this description thing work?.",
  "URL": "http://localhost:8000/test.zip",
  "Images": ["http://localhost:8000/test2.jpg"]
},
{
  "Name": "%s repo 3",
  "Program": "i3",
  "Description": "test.",
  "URL": "http://localhost:8000/test.zip",
  "Images": ["http://localhost:8000/test3.png"]
}
]""" % (self.path[1:], self.path[1:], self.path[1:])
    self.wfile.write(bytes(out, "utf-8"))

myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
  myServer.serve_forever()
except KeyboardInterrupt:
  pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
