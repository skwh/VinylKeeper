import json
import os
import signal
import sys
from BaseHTTPServer import BaseHTTPRequestHandler
from SocketServer import TCPServer

from vk_database import VKDatabase

_MIME_TYPES = {
    '.txt': 'text/plain',
    '.bin': 'application/octet-stream',
    '.css': 'text/css',
    '.gif': 'image/gif',
    '.htm': 'text/html',
    '.html': 'text/html',
    '.ico': 'image/x-icon',
    '.jar': 'application/java-archive',
    '.js': 'application/javascript',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.json': 'application/json',
    '.otf': 'font/otf',
    '.png': 'image/png',
    '.pdf': 'application/pdf',
    '.svg': 'image/svg+xml',
    '.tar': 'application/x-tar',
    '.ttf': 'font/ttf',
    '.woff': 'font/woff',
    '.woff2': 'font/woff2',
    '.xhtml': 'application/xhtml+xml',
    '.xml': 'application/xml',
    '.zip': 'application/zip'
}

class VKServer:
    def __init__(self, port_number, database_path):
        if type(port_number) is not int or type(database_path) is not str:
            raise TypeError
        else:
            self.port_number = port_number
            self.database = database_path
        self.database_handler = VKDatabase(self.database)
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
        request.reply(json.dumps(results), _MIME_TYPES['.json'])

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
        self.METHOD_PATHS = paths
        self.METHOD_PATHS['/pathz'] = self._pathz
        self._PROJECT_ROOT = project_root
        self._FILE_PATHS = {
            '' : self._PROJECT_ROOT + 'index.html',
            '/' : self._PROJECT_ROOT + 'index.html'
        }
        self._generate_filetree("")

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
                self._FILE_PATHS[relative_path] = full_file_path
            else:
                # If the filename is a directory, generate a tree for it.
                self._generate_filetree(filename)

    def _serve_file(self, path_to_file):
        try:
            file_contents = open(path_to_file, 'r').read()
            file_extension = os.path.splitext(path_to_file)[1]
            file_type = self._get_mime_type(file_extension)
            self._send_string(file_contents, 200, "OK", file_type)
        except Exception as e:
            print e
            self.send_error(500)

    def _send_string(self, string, code, message, content_type):
        content_length = sys.getsizeof(string)
        self.log_request(code, content_length)
        self.send_response(code, message)
        self.send_header('Content-type:', content_type)
        self.send_header('Content-Length:', content_length)
        self.end_headers()
        self.wfile.write(string)
        self.wfile.flush()

    def reply(self, contents, mime_type='text/plain'):
        if type(contents) is str and os.path.isfile(contents):
            self._serve_file(contents)
        else:
            self._send_string(contents, 200, "OK", mime_type)

    def _route(self, path):
        """Path is relative to the domain root: /index.html, /home, etc"""
        # Detect if route is in _FILE_PATHS
        if path in self._FILE_PATHS:
            # Serve file content
            self._serve_file(self._FILE_PATHS[path])
        # Detect if route is in METHOD_PATHS
        elif path in self.METHOD_PATHS:
            # Call the provided method
            self.METHOD_PATHS[path](self)
        else:
            self.send_error(404)

    def _pathz(self, request):
        del request
        content = ("FILE PATHS: %s"
                   "METHOD PATHS: %s") % (self._FILE_PATHS, self.METHOD_PATHS)
        self.reply(content, 'text/plain')

    def _statusz(self, request):
        self.reply(request.server.status(), 'text/plain')

    def do_GET(self):
        self._route(self.path)

    def do_HEAD(self):
        print "HEAD request received"

    def _get_mime_type(self, extension):
        return _MIME_TYPES[extension]
