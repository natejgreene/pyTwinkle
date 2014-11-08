from broadcaster import Broadcaster
from light_strand import LightStrand
from server import Server
import Queue

command_queue = Queue.Queue()
strands = LightStrand.connect_all_strands()

#start the server
server = Server(command_queue)
server.start()

#start the broadcaster
broadcaster = Broadcaster(strands, command_queue)
broadcaster.start()

