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
        if loops is not None:
            self.loops = loops
        if light_count is not None:
            self.light_count = light_count

    def stop(self):
        self.runnable = False

    def program(self):
        pass

    def run(self):
        while self.runnable and self.loops != 0:
            self.program()
            if self.loops > 0:
		self.loops -= 1

    def send_command(self, command_string):
        command = binascii.unhexlify(command_string)
        self.command_queue.put(command)

class CandyCane(LightProgram):
    def program(self):
        repeat_count = 3
        for p in range(0,2):
            command_string = []
            for i in range(self.light_count):
                color = "0F0F0F"
                if i % 2 == p:
                    color = "00000F"
                for x in range(repeat_count):
                    command_string.append("FF06{:02X}FE{}000000FF".format(i , color))

            self.send_command("".join(command_string))
            time.sleep(.5)

class CandyCorn(LightProgram):
    def program(self):
        repeat_count = 3
        color_list = ["000A0F","000F0F", "0F0F0F"]
        color_list_len = len(color_list)
        command_string = []
        for i in range(self.light_count):
            color = color_list[i % color_list_len]
            for x in range(repeat_count):
                command_string.append("FF06{:02X}FE{}000000FF".format(i , color))

        self.send_command("".join(command_string))

class Cylon(LightProgram):

    position = 0
    direction = 1
    def program(self):
        repeat_count = 3
        width = 5
        command_string = []
        for i in range(0, self.light_count):
            if self.position != i:
                color = "000000"
            else:
                color = "00000F"
            for x in range(repeat_count):
                command_string.append("FF06{:02X}FE{}000000FF".format(i , color))

        self.send_command("".join(command_string))

        if self.position > self.light_count:
            self.direction = -1
        elif self.position <= 0:
            self.direction = 1

        self.position = self.position + self.direction

        time.sleep(.1)
