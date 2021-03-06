import bluetooth
import sys

LIGHTS_NAME = "00651 36L RGB"

class LightStrand:

    address = None
    port = None
    socket = None
    connected = False

    def __init__(self, address, port):
        self.address = address
        self.port = port

    def __del__(self):
        if self.socket:
            self.socket.close()

    def __connect(self):
        try:
            self.socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
            self.socket.connect((self.address, self.port))
            self.connected = True
            print "Connected to:", self.address
            sys.stdout.flush()
        except:
            self.connected = False
            print "Could not connect to:", self.address
            sys.stdout.flush()

    def send(self,command):
        try:
            if self.connected:
                self.socket.send(command)
        except:
            print "Error sending command to ", self.address
            sys.stdout.flush()
            self.connected = False

    @staticmethod
    def connect_all_strands():
        nearby_devices = bluetooth.discover_devices()

        strands = []
        for bdaddr in nearby_devices:
            if LIGHTS_NAME == bluetooth.lookup_name( bdaddr ):
                strand = LightStrand(bdaddr,6)
                strand.__connect()
                strands.append(strand)

        return strands
