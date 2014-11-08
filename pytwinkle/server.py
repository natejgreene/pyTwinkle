import bluetooth
import Queue
import threading
import sys

class Server:

    server_socket = None
    client_socket = None

    command_queue = None
    stop_thread = False

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
            bluetooth.advertise_service(self.server_socket, "pyTwinkle", service_classes = [ bluetooth.SERIAL_PORT_CLASS ], profiles = [ bluetooth.SERIAL_PORT_PROFILE ] )
        except:
            print >>sys.stderr, "Could not start a bluetooth server."
            sys.stdout.flush()
            sys.exit(1)
        t = threading.Thread(target=self.__run)
        t.daemon = True
        t.start()

    def stop(self):
       self.stop_thread = True

    def __run(self):
        print "Running"
        sys.stdout.flush()
        while not self.stop_thread:
            self.client_socket, address = self.server_socket.accept()
            sys.stdout.flush()
            while True:
                try:
                    self.command_queue.put(self.client_socket.recv(10))
                except:
                    print "Server lost connection from client."
                    sys.stdout.flush()
                    break




