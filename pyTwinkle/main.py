from broadcaster import *
from light_strand import *
from server import *
from program import *
import Queue
import binascii

command_queue = Queue.Queue()
strands = LightStrand.connect_all_strands()

#start the bluetooth server
server = Server(command_queue)
server.start()

#start the broadcaster
broadcaster = Broadcaster(strands, command_queue)
broadcaster.start()

p = None
while True:
    try:
        print "1. Candy Cane"
        print "2. Cylon"
        print "q. Quit"
        print 30 * "-"
        selection=raw_input("Enter Option:")
        if p is not None:
            p.stop()

        if selection =='1':
            p = CandyCane(command_queue).start()
        elif selection =='2':
            p = Cylon(command_queue).start()
        elif selection =='r':
            selection2=raw_input("Enter Raw:")
            command = binascii.unhexlify(selection2)
            command_queue.put(command)
        elif selection =='s':
            pass
        elif selection =='q':
            exit(0)

    except (KeyboardInterrupt, SystemExit):
        server.stop()
        broadcaster.stop()
        print "Exiting..."
        break

