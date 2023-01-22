from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        from cloudlink import cloudlink
        cl = cloudlink()
        server = cl.server(logs=False)
        server.run(ip = "0.0.0.0",port = 3000)
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return
