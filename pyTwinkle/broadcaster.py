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
        t = threading.Thread(target=self.__broadcast)
        t.daemon = True
        t.start()

    def __broadcast(self):
        if self.command_queue:
            while True:
                if not self.command_queue.empty():
                    data = self.command_queue.get()
                    for strand in self.light_strands:
                        strand.send(data)
                    self.command_queue.task_done()
