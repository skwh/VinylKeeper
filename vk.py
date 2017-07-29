import sys

from vk_server import VKServer

DEFAULT_PORT_NUMBER = 80
DEFAULT_DATABASE_PATH = "database.db"


def main(argv):
    args = extract_args(argv)
    port, database_path = get_server_args(args)
    server = VKServer(int(port), database_path)
    server.start()


# TODO: Reorganize these util methods
def extract_args(argv):
    """Extracts argument pairs from sys.argv."""
    args = []
    for val in argv:
        kv = val[1:]
        key, value = (kv.split('=')[0], kv.split('=')[1])
        args.append((key, value))
    return args


def get_server_args(args):
    """Extracts the port and database path from a list of arguments."""
    port = DEFAULT_PORT_NUMBER
    database_path = DEFAULT_DATABASE_PATH
    for val in args:
        if val[0] == "port":
            port = val[1]
        elif val[0] == "database" or val[0] == "database_path":
            database_path = val[1]
    return port, database_path

if __name__ == '__main__':
    main(sys.argv[1:])
