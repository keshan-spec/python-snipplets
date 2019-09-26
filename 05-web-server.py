import http.server
import socketserver

handler = http.server.SimpleHTTPRequestHandler

try:
    with socketserver.TCPServer(('', 5000), handler) as httpd:
        print("[+] Starting server..")
        print("[+] Server started at http://localhost:5000/")
        httpd.serve_forever()

except KeyboardInterrupt:
    print("[-] SERVER STOPPED")
    pass
