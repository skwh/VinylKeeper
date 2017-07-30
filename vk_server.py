import os
import signal
import sys
from BaseHTTPServer import BaseHTTPRequestHandler
from SocketServer import TCPServer

from vk_database import VKDatabase


class VKServer:
    def __init__(self, port_number, database_path):
        if type(port_number) is not int or type(database_path) is not str:
            raise TypeError
        else:
            self.port_number = port_number
            self.database = database_path
        self.database_handler = VKDatabase(self.database)
        # TODO: re-write handler for Angular & database api usage
        self.request_handler = ExtensibleHTTPRequestHandler({
            '/api/GetRecords': self.GetRecords
        }, project_root='./VinylKeeper/dist/')
        # TODO: args & handling for server address
        self.http_server = TCPServer(("0.0.0.0", port_number), self.request_handler)
        self._register_sigint()
        self.status = 'Ready'

    def _register_sigint(self):
        # TODO: sigint graceful shutdown
        signal.signal(signal.SIGINT, self.stop)

    def _print_address(self):
        return "%s:%i" % self.http_server.server_address

    def GetRecords(self, request):
        results = self.database_handler.get_records()
        request.reply(results)

    def status(self):
        return self.status

    def start(self):
        print "Starting server at %s..." % self._print_address()
        self.status = 'Serving'
        self.http_server.serve_forever()

    def stop(self):
        print "Shutting down."
        self.status = 'Stopping'
        self.http_server.shutdown()
        self.http_server.server_close()
        print "Shut down successfully."
        self.status = 'Shutdown'
        return 0


class ExtensibleHTTPRequestHandler(BaseHTTPRequestHandler):
    def __call__(self, request, client_address, server):
        self.request = request
        self.client_address = client_address
        self.server = server
        self.rfile = self.request.makefile()
        self.wfile = self.request.makefile()
        self.handle()

    def __init__(self, paths, project_root='./'):
        """Set up default paths and their handlers."""
        self.PROVIDED_PATHS = paths
        self._PROJECT_ROOT = project_root
        self._DEFAULT_PATHS = {
            '' : self._PROJECT_ROOT + 'index.html',
            '/' : self._PROJECT_ROOT + 'index.html'
        }
        self._generate_filetree("")
        print self._DEFAULT_PATHS

    def _generate_filetree(self, path):
        """Generates a dict with path maps."""
        # Get the full path to the project root to detect static files.
        full_path = os.path.join(self._PROJECT_ROOT, path)
        # Get a list of those files.
        path_files = os.listdir(full_path)
        # Iterate over those files.
        for filename in path_files:
            # Get the full path to the file.
            full_file_path = os.path.join(full_path, filename)
            # If the filename is a file, add it to the map.
            if os.path.isfile(full_file_path):
                # Map structure: relative_path: file_path
                relative_path = os.path.join("/", path, filename)
                self._DEFAULT_PATHS[relative_path] = full_file_path
            else:
                # If the filename is a directory, generate a tree for it.
                self._generate_filetree(filename)

    def _get_file_contents(self, filename):
        try:
            return open(filename, 'r').read()
        except IOError as e:
            self.send_error(500, e.message)

    def _serve_file(self, filename):
        self._serve_text(self._get_file_contents(filename))

    def _serve_text(self, string):
        try:
            self._send_content(string, 200, "SURE OK THEN")
        except IOError as e:
            self.send_error(500, e.message)

    def _send_content(self, object, code, message):
        content_type = 'text/html'
        content_length = sys.getsizeof(object)
        self.send_response(code, message)
        self.send_header('Content-type:', content_type)
        self.send_header('Content-Length:', content_length)
        self.end_headers()
        self.wfile.write(object)
        self.wfile.flush()

    def reply(self, contents):
        self._send_content(contents, 200, "OK")

    def _route(self, path):
        """Path is relative to the domain root: /index.html, /home, etc"""
        # Detect if route is in DEFAULT_PATHS
        if self._DEFAULT_PATHS[path]:
            # Serve file content
            self._serve_file(self._DEFAULT_PATHS[path])
        # Detect if route is in PROVIDED_PATHS
        elif self.PROVIDED_PATHS[path]:
            # Call the provided method
            self.PROVIDED_PATHS[path](self)



    def do_GET(self):
        self._route(self.path)

    def do_HEAD(self):
        print "HEAD request received"
