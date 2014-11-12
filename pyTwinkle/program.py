import threading
import binascii
import time

class LightProgram(threading.Thread):

    runnable = True
    loops = -1
    command_queue = None
    light_count = 36

    def __init__(self, command_queue, light_count=None, loops=None):
        threading.Thread.__init__(self)
        self.command_queue = command_queue
        self.daemon = True
        if self.loops is not None:
            self.loops = loops
        if self.light_count is not None:
            self.light_count = light_count

    def stop(self):
        self.runnable = False

    def program(self):
        pass

    def run(self):
        while self.runnable and self.loops != 0:
            self.program()
            self.loops -= 1

    def send_command(self, command_string):
        command = binascii.unhexlify(command_string)
        self.command_queue.put(command)


class CandyCane(LightProgram):
    def program(self):
        repeat_count = 3
        for p in range(0,2)
            command_string = []
            for i in range(self.light_count):
                color = "0F0F0F"
                if i % 2 == p:
                    color = "00000F"
                for x in range(repeat_count)
                    command_string.append("FF06{:02X}FE{}000000FF".format(i , color))

            self.send_command("".join(command_string))
            time.sleep(.5)


class Scanner(LightProgram):
    def program(self):
        repeat_count = 3
        width = 5
        color = "00000F"
        command_string = []
        for i in range(self.light_count):

            for j in range(width):
                for x in range(repeat_count)
                    command_string.append("FF06{:02X}FE{}000000FF".format(i , color))


        self.send_command("".join(command_string))
        time.sleep(.3)
