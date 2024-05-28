import http.server
import json
import psycopg2
import os

class HandlerRequest(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_path = os.path.join(os.getcwd(), self.path[1:])
            with open(file_path, 'r', encoding='utf-8') as file:
                file_to_open = file.read()

            # file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except Exception as e:
            print(f'Error: {e}')
            file_to_open = 'File not found'
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        user_data = json.loads(post_data)

        conn = psycopg2.connect('dbname=Hospital user=postgres password=1234')
        cur = conn.cursor()

        if self.path == '/register':
            cur.execute("SELECT * FROM Users WHERE login = %s", (user_data['username'],))
            existing_user = cur.fetchone()

            if existing_user:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'User already exists')
            else:
                cur.execute("INSERT INTO Users (Name, LastName, Phone, Login, Password) VALUES (%s, %s, %s, %s, %s)", (user_data['firstname'], user_data['lastname'], user_data['phone'], user_data['username'], user_data['password'],))
                conn.commit()

                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'Registration successful')

        elif self.path == '/login':
            cur.execute("SELECT * FROM Users WHERE login = %s AND password = %s", (user_data['login'], user_data['password'],))
            existing_user = cur.fetchone()
            if existing_user:
                role = existing_user[6]
                if role == 1:
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b'Successful autorization')
                else:
                    self.send_response(201)
                    self.end_headers()
                    self.wfile.write(b'Successful autorization')
            else:
                self.response(401)
                self.end_headers()
                self.wfile.write(b'Invalid username or password')
        else:
            self.response(404)
            self.end_headers()
            self.wfile.write(b'Not found')

        cur.close()
        conn.close()


def run(server_class=http.server.HTTPServer, handler_class=HandlerRequest):
  server_address = ('', 8000)
  httpd = server_class(server_address, handler_class)
  httpd.serve_forever()

run()
