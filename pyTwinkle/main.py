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
        selection=raw_input("Connect Mobile or Enter Option:")
        if p is not None:
            p.stop()

        if selection =='1':
            p = program.CandyCane(command_queue).start()
        if selection =='2':
            p = program.Scanner(command_queue).start()
        elif selection =='r':
            selection2=raw_input("Enter Raw:")
            command = binascii.unhexlify(selection2)
            command_queue.put(command)
        elif selection =='s':
            pass
        elif selection =='e':
            exit(0)

    except (KeyboardInterrupt, SystemExit):
        server.stop()
        broadcaster.stop()
        print "Exiting..."
        break

