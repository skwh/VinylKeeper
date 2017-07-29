import SimpleHTTPServer
import SocketServer
import signal

from vk_database import VKDatabase


class VKServer:
    def __init__(self, port_number, database_path):
        if type(port_number) is not int or type(database_path) is not str:
            raise TypeError
        else:
            self.port_number = port_number
            self.database = database_path
        # TODO: re-write handler for Angular & database api usage
        self.request_handler = SimpleHTTPServer.SimpleHTTPRequestHandler
        # TODO: args & handling for server address
        self.http_server = SocketServer.TCPServer(("0.0.0.0", port_number), self.request_handler)
        self.database_handler = VKDatabase(self.database)
        self._register_sigint()
        self.status = 'Ready'

    def _register_sigint(self):
        # TODO: sigint graceful shutdown
        signal.signal(signal.SIGINT, self.stop)

    def _print_address(self):
        return "%s:%i" % self.http_server.server_address

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

