import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from views import get_all_employees, get_single_employee, create_employee, update_employee, delete_employee
from views import get_all_products, get_single_product, create_product, update_product, delete_product
from views import get_all_orders, get_single_order, create_order, update_order, delete_order



class HandleRequests(BaseHTTPRequestHandler):
    """Handles the requests to this server"""

    def parse_url(self, path):
        """Parse the url into the resource and id"""
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split('/')
        resource = path_params[1]

        if parsed_url.query:
            query = parse_qs(parsed_url.query)
            return (resource, query)

        pk = None
        try:
            pk = int(path_params[2])
        except (IndexError, ValueError):
            pass
        return (resource, pk)

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the OPTIONS headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        """Handle Get requests to the server"""
        status_code = 200
        response = {}

        (resource, id) = self.parse_url(self.path)

        if resource == "products":
            if id is not None:
                response = get_single_product(id)
                if response is None:
                    status_code = 404
                    response = {"message": "That product is not currently in stock."}
            else:
                response = get_all_products()

        if resource == "employees":
            if id is not None:
                response = get_single_employee(id)
                if response is None:
                    status_code = 404
                    response = {"message": "That employee does not exist."}
            else:
                response = get_all_employees()

        if resource == "orders":
            if id is not None:
                response = get_single_order(id)
                if response is None:
                    status_code = 404
                    response = {"message": "That order does not exist."}
            else:
                response = get_all_orders()

        self._set_headers(status_code)
        self.wfile.write(json.dumps(response).encode())
       
    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)
        new_product = None
        new_employee = None
        new_order = None

        if resource == "employees":
            new_employee = create_employee(post_body)
            self.wfile.write(json.dumps(new_employee).encode())

        if resource == "products":
            new_product = create_product(post_body)
            self.wfile.write(json.dumps(new_product).encode())

        if resource == "orders":
            new_order = create_order(post_body)
            self.wfile.write(json.dumps(new_order).encode())
        

    def do_PUT(self):
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        if resource == "employees":
            update_employee(id, post_body)

        if resource == "products":
            update_product(id, post_body)

        if resource == "orders":
            update_order(id, post_body)

        self.wfile.write("".encode())
        
    def do_DELETE(self):
        self._set_headers(204)

        (resource, id) = self.parse_url(self.path)

        if resource == "employees":
            delete_employee(id)
        
        if resource == "orders":
            delete_order(id)
        
        if resource == "products":
            delete_product(id)

        self.wfile.write("".encode())


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
