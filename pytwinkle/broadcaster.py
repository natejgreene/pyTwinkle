import Queue
import threading
import sys
from light_strand import LightStrand

class Broadcaster:

    light_strands = None
    command_queue = None
    stop_thread = False

    def __init__(self, light_strands, command_queue):
        self.light_strands = light_strands
        self.command_queue = command_queue

    def start(self):
        threading.Thread(target=self.__broadcast).start()

    def stop(self):
        self.stop_thread = True

    def __broadcast(self):
        if self.command_queue:
            while not self.stop_thread:
                if not self.command_queue.empty():
                    data = self.command_queue.get()
                    for strand in self.light_strands:
                        strand.send(data)
                    self.command_queue.task_done()
