import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from views import get_all_employees, get_single_employee, get_all_products, get_single_product
from views import get_all_orders, get_single_order



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
        """Make a post request to the server"""

    def do_PUT(self):
        """Handles PUT requests to the server"""

    def do_DELETE(self):
        """Handle DELETE Requests"""


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
