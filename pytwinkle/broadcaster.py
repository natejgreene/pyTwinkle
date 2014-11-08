import Queue
import threading
import sys
from light_strand import LightStrand

class Broadcaster:

    light_strands = None
    command_queue = None

    def __init__(self, light_strands, command_queue):
        self.light_strands = light_strands
        self.command_queue = command_queue

    def start(self):
        threading.Thread(target=self.__broadcast).start()

    def __broadcast(self):
        if self.command_queue:
            while True:
                if not self.command_queue.empty():
                    print "Get from queue"
                    sys.stdout.flush()
                    data = self.command_queue.get()
                    print "Sending to strands."
                    sys.stdout.flush()
                    for strand in self.light_strands:
                        strand.send(data)
                    self.command_queue.task_done()
