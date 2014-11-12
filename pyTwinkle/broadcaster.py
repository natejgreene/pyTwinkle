import Queue
import threading
import sys
from light_strand import *

class Broadcaster:

    light_strands = None
    command_queue = None
    runnable = True

    def __init__(self, light_strands, command_queue):
        self.light_strands = light_strands
        self.command_queue = command_queue

    def start(self):
        t = threading.Thread(target=self.__broadcast)
        t.start()

    def stop(self):
        self.runnable = False

    def __broadcast(self):
        if self.command_queue:
            while self.runnable:
                if not self.command_queue.empty():
                    data = self.command_queue.get()
                    for strand in self.light_strands:
                        strand.send(data)
                    self.command_queue.task_done()
