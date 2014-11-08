import bluetooth
import Queue
import threading

class Server:

    server_socket = None
    client_socket = None

    command_queue = None

    def __init__(self, command_queue):
        self.command_queue = command_queue

    def __del__(self):
        if self.server_socket:
            self.server_socket.close()
        if self.client_socket:
            self.client_socket.close()

    def start(self):
        try:
            self.server_socket = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
            self.server_socket.bind(("", bluetooth.PORT_ANY))
            self.server_socket.listen(1)
            bluetooth.advertise_service(self.server_socket, "itwinkle repeater", service_classes = [ bluetooth.SERIAL_PORT_CLASS ], profiles = [ bluetooth.SERIAL_PORT_PROFILE ] )
        except:
            print >>sys.stderr, "Could not start a bluetooth server."
            sys.exit(1)
        threading.thread(target="__run").start()

    def __run(self):
        while True:
            self.client_socket, address = self.__server_socket.accept()
            while True:
                try:
                    command_queue.put(self.client_socket.recv(10))
                except:
                    print "Server lost connection from client."
                    break



