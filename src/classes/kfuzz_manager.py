from queue import Queue

from src.classes.executor import Executor
from src.classes.thread_wrapper import ThreadWrapper


class KfuzzManager:

    def __init__(self, target, argument_generator, t, threads):
        self.target = target
        self.argument_generator = argument_generator
        self.t = t
        self.threads = threads
        self.queue = Queue()
        self.run()
        self.__get_generator()
        self.add_to_queue(self.target)
        self.results = []


    def add_to_queue(self, target):
        for argument in self.argument_generator:
            self.queue.put(Executor(target, argument, self.t))

    def __get_generator(self):
        if type(self.argument_generator) == list:
            pass
        else:
            self.argument_generator = self.argument_generator.generator()

    def run(self):
        for i in range(self.threads):
            t = ThreadWrapper(self.queue, self)
            t.setDaemon(True)
            t.start()

        self.queue.join()
