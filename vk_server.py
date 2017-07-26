import SimpleHTTPServer
import SocketServer
import signal

from vk_database import VKDatabase


class VKServer:
    def __init__(self, port_number, database_path):
        self.port_number = port_number
        self.database = database_path
        # TODO: re-write handler for Angular & database api usage
        self.request_handler = SimpleHTTPServer.SimpleHTTPRequestHandler
        # TODO: args & handling for server address
        self.http_server = SocketServer.TCPServer(("0.0.0.0", port_number), self.request_handler)
        self.database_handler = VKDatabase(self.database)
        self._register_sigint()

    def _register_sigint(self):
        # TODO: sigint graceful shutdown
        signal.signal(signal.SIGINT, self.stop)

    def _print_address(self):
        return "%s:%i" % self.http_server.server_address

    def start(self):
        print "Starting server at %s..." % self._print_address()
        self.http_server.serve_forever()

    def stop(self):
        print "Shutting down."
        self.http_server.shutdown()
        self.http_server.server_close()
        print "Shut down successfully."
        return 0

