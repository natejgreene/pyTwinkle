from broadcaster import Broadcaster
from light_strand import LightStrand
from server import Server
from program_runner import ProgramRunner
import Queue
import time
import binascii


command_queue = Queue.Queue()
strands = LightStrand.connect_all_strands()

#start the server
server = Server(command_queue)
server.start()

#start the broadcaster
broadcaster = Broadcaster(strands, command_queue)
broadcaster.start()

def candy_cane():
    for i in range(35):
        color = "0F0F0F"
        if i % 2:
            color = "00000F"

        command_string = "FF06{:02X}FE{}000000".format(i , color)
        command = binascii.unhexlify(command_string)
        command_queue.put(command)

    time.sleep(.5)

    for i in range(35):
        color = "00000F"
        if i % 2:
            color = "0F0F0F"

        command_string = "FF06{:02X}FE{}000000".format(i , color)
        command = binascii.unhexlify(command_string)
        command_queue.put(command)

    time.sleep(.5)

program = None
while True:
    try:
        selection=raw_input("Connect Mobile or Enter Option:")
        if program:
            program.stop()
        if selection =='1':
            program = ProgramRunner(candy_cane).start
        elif selection =='s':
            pass
        elif selection =='e':
            exit(0)

    except (KeyboardInterrupt, SystemExit):
        server.stop()
        broadcaster.stop()
        print "Exiting..."
        break

