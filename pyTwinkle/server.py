import bluetooth
import Queue
import threading
import sys

class Server(threading.Thread):

    server_socket = None
    client_socket = None
    command_queue = None
    runnable = True

    def __init__(self, command_queue):
        self.command_queue = command_queue
        super(self.__class__, self).__init__()

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
            self.server_socket.settimeout(5)
            bluetooth.advertise_service(self.server_socket, "pyTwinkle", service_classes = [ bluetooth.SERIAL_PORT_CLASS ], profiles = [ bluetooth.SERIAL_PORT_PROFILE ] )
	    super(self.__class__, self).start()
        except:
            print >>sys.stderr, "Could not start a bluetooth server."
            sys.stdout.flush()

    def stop(self):
        self.runnable = False

    def run(self):
        print "Bluetooth Server Started..."
        sys.stdout.flush()
        while self.runnable:
            try:
                self.client_socket, address = self.server_socket.accept()
            except:
                continue

            while self.runnable:
                try:
                    self.command_queue.put(self.client_socket.recv(10))
                except:
                    print "Server lost connection from client."
                    sys.stdout.flush()
                    break




