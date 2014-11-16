import Queue
import threading
import sys
from light_strand import *

class Broadcaster(threading.Thread):

    light_strands = None
    command_queue = None
    runnable = True

    def __init__(self, light_strands, command_queue):
        self.light_strands = light_strands
        self.command_queue = command_queue
        super(self.__class__, self).__init__()

    def stop(self):
        self.runnable = False

    def run(self):
        if self.command_queue:
            while self.runnable:
                if not self.command_queue.empty():
                    data = self.command_queue.get()
                    for strand in self.light_strands:
                        strand.send(data)
                    self.command_queue.task_done()
