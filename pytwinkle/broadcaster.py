import Queue
import threading
import light_strand

class Broadcaster:
    light_strands = None
    command_queue = None

    def __init__(self, light_strands, command_queue):
        self.light_strands = light_strands
        self.command_queue = commend_queue

    def start():
        threading.Thread(target="__broadcast").start()

    def __broadcast(self):
        if self.command_queue:
            while True:
                for strand in light_strands:
                  strand.send(command_queue.get())