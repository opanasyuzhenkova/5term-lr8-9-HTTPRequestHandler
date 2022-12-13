from http.server import HTTPServer
import simplemvcapp

HOST = "0.0.0.0"
PORT = 8000

# Запуск локального сервера
httpd = HTTPServer(('localhost', 8000), simplemvcapp.package.handler.SimpleHTTPRequestHandler)
print("Server running...")
httpd.serve_forever()
httpd.server_close()
print("Server stopped!")
