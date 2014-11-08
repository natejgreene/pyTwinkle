class Server:

    server_socket = None
    client_socket = None
    light_strands = []
    def start(self):
        try:
            import bluetooth
        except:
            print >>sys.stderr, "Python module pybluez not installed."
            sys.exit(1)
        try:
            self.server_socket = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
            self.server_socket.bind(("", bluetooth.PORT_ANY))
            self.server_socket.listen(1)
            bluetooth.advertise_service(self.server_socket, "itwinkle repeater", service_classes = [ bluetooth.SERIAL_PORT_CLASS ], profiles = [ bluetooth.SERIAL_PORT_PROFILE ] )
        except:
            print >>sys.stderr, "Could not start a bluetooth server."
            sys.exit(2)
        self.__setup_light_strands()
        self.__run()

    def __del__(self):
        if self.server_socket:
            self.server_socket.close()
        if self.client_socket:
            self.client_socket.close()

    def __run(self):
        while True:
            self.client_socket, address = self.__server_socket.accept()
            while True:
                try:
                    data = client_sock.recv(10)
                    for strand in light_strands:
                        strand.send(data)
                except (KeyboardInterrupt, SystemExit):
                    print "Exiting..."
                    break;
                except:
                    print "An Error Occurred"


    def __setup_light_strands(self):
        lights_name = "00651 36L RGB"

        nearby_devices = bluetooth.discover_devices()

        addresses = []
        for bdaddr in nearby_devices:
            if lights_name == bluetooth.lookup_name( bdaddr ):
                addresses.append(bdaddr)
                print "Found: %s", bdaddr

        print "Found %d light strands" % len(addresses)

        for bdaddr in addresses:
            try:
                sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
                sock.connect((bdaddr, 6))
                light_strands.append(sock)
                print "Connect: %s" % bdaddr
            except:
                print "Connect Failed: %s" % bdaddr
