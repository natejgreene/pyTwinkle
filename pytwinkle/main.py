from broadcaster import Broadcaster
from light_strand import LightStrand
from server import Server
import Queue
import time

  try:
command_queue = Queue.Queue()
strands = LightStrand.connect_all_strands()

#start the server
server = Server(command_queue)
server.start()

#start the broadcaster
broadcaster = Broadcaster(strands, command_queue)
broadcaster.start()

while True:
    try:
        time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        print "Exiting..."
        server.stop()
        broadcaster.stop()
