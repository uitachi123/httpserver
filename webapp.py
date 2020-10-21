import SimpleHTTPServer
import SocketServer

PORT = 8000

# Create the server, binding to localhost on port 9999
server = SocketServer.TCPServer(("", PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)

# Activate the server; this will keep running until you
# interrupt the program with Ctrl-C
server.serve_forever()