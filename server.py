import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from repository import all, retrieve, create, update, delete, DATABASE

method_mapper = {
    "employees": {
        "single": retrieve,
        "all": all
    },
    "products": {
        "single": retrieve,
        "all": all
    },
    "orders": {
        "single": retrieve,
        "all": all
    }
}

class HandleRequests(BaseHTTPRequestHandler):
    """Handles the requests to this server"""

    def get_all_or_single(self, resource, id):
        """DRY function for getting all or single resources"""
        if id is not None:
            response = method_mapper[resource]["single"](resource, id)

            if response is not None:
                self._set_headers(200)
            else:
                self._set_headers(404)
                response = {"message": f'{resource} {id} does not exist'}
        else:
            self._set_headers(200)
            response = method_mapper[resource]["all"](resource)

        return response

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
        response = None
        (resource, id) = self.parse_url(self.path)
        response = self.get_all_or_single(resource, id)
        self.wfile.write(json.dumps(response).encode())
       
    def do_POST(self):
        """Create New Resource."""
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id) = self.parse_url(self.path)
        new_resource = None
        
        required_fields = {
            "employees": ["name", "email", "hourly_rate"],
            "products": ["name", "price"],
            "orders": ["product_id", "employee_id", "timestamp"]
        }

        if resource in required_fields:
            missing_fields = [
                field for field in required_fields[resource] if field not in post_body
            ]
            if not missing_fields:
                self._set_headers(201)
                new_resource = create(resource, post_body)
                self.wfile.write(json.dumps(new_resource).encode())
            else:
                self._set_headers(400)
                message = {"message": "".join(
                    [f"{field} is required" for field in missing_fields]
                )
                }
                self.wfile.write(json.dumps(message).encode())
        else:
            self._set_headers(400)
            message = {"message": "Resource not valid"}
            self.wfile.write(json.dumps(message).encode())

    def do_PUT(self):
        """Handles PUT requests to server"""
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)
        update(resource, id, post_body)

        self.wfile.write("".encode())
        
    def do_DELETE(self):
        """Handles DELETE requests to server"""
        (resource, id) = self.parse_url(self.path)

        if resource == "employees":
            if len(DATABASE["employees"]) > 1:
                self._set_headers(204)
                delete(resource, id)
            else:
                self._set_headers(405)
                delete_employee_message = {
                    "message": 'Cannot delete the only employee willing to work.'
                }
                self.wfile.write(json.dumps(delete_employee_message).encode())
        
        else:
            self._set_headers(204)
            delete(resource, id)

            self.wfile.write("".encode())


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
