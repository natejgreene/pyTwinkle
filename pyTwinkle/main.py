from broadcaster import *
from light_strand import *
from server import *
import program
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
def start_program(name):
    global p
    if p is not None:
        p.stop()
    p = getattr(globals()['program'], name)(command_queue)
    p.start()

while True:
    try:
        print "1. Candy Cane"
        print "2. Cylon"
        print "3. Candy Corn"
        print "s. Stop"
        print "q. Quit"
        print 30 * "-"
        selection=raw_input("Enter Option:")

        if selection =='1':
            start_program('CandyCane')
        elif selection =='2':
            start_program('Cylon')
        elif selection =='3':
            start_program('CandyCorn')
    	elif selection == 's':
            p.stop()
        elif selection =='r':
            selection2=raw_input("Enter Raw:")
            command = binascii.unhexlify(selection2)
            command_queue.put(command)
        elif selection =='q':
            exit(0)

    except (KeyboardInterrupt, SystemExit):
        server.stop()
        broadcaster.stop()
        print "Exiting..."
        break

