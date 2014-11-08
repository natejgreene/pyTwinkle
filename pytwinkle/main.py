import broadcaster
import light_strand
import server
import Queue

command_queue = Queue()
strands = light_strand.connect_all_strands()

#start the server
server = Server(command_queue)
server.start()

#start the broadcaster
broadcaster = Broadcaster(strands, command_queue)
broadcaster.start()

