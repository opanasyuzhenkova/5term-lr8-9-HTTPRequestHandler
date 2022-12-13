import json
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
from jinja2 import Environment, PackageLoader
from . import users


def load_templates(list_of_users):
    env = Environment(loader=PackageLoader('simplemvcapp', 'templates'))
    template = env.get_template('layout.html')
    return template.render(list_of_users=list_of_users)


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        list_of_users = users.get_users_lst()
        self.wfile.write(bytes(load_templates(list_of_users), "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html, charset="utf-8"')
        self.end_headers()
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = urllib.parse.parse_qs(str(body, 'utf-8'), keep_blank_values=True)
        data = {k: v[0] for k, v in data.items()}
        print(data)
        result = bytes(data['user'], 'utf-8') + bytes(" : ", 'utf-8') + bytes(data['pass'], 'utf-8') + bytes(" : ", 'utf-8') \
                 + bytes(data['surname'], 'utf-8') + bytes(" : ", 'utf-8') + bytes(data['section'], 'utf-8') + \
                 bytes(" : ", 'utf-8')  + bytes(data['mail'], 'utf-8')

        self.wfile.write(result)
        users_json = json.dumps(data)

        with open("users.json", "w") as my_file:
            my_file.write(users_json)


