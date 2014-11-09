import threading

class ProgramRunner (threading.Thread):

    program_method = None
    runnable = True

    def __init__(self, program_method):
        threading.Thread.__init__(self)
        self.daemon = True
        self.program_method = program_method

    def stop(self):
        self.runnable = False

    def run(self):
        while self.runnable:
            self.program_method()




