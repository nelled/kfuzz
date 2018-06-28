import signal
import subprocess as sub

from tabulate import tabulate


class Executor:

    def __init__(self, target, argument, t):
        self.target = target
        self.argument = argument
        self.t = t
        self.__execution_successful = False
        self.__stdout = ''
        self.__signal = -1

    @property
    def execution_successful(self):
        return self.__execution_successful

    @property
    def stdout(self):
        return self.__stdout

    @property
    def signal(self):
        return self.__signal

    def do_execute(self):
        try:
            output = sub.run(args=self.target + " " + self.argument, stdout=sub.PIPE, stderr=sub.STDOUT, shell=True,
                             check=True)
            self.__stdout = output.stdout.decode('utf-8')
            self.__signal = output.returncode
            self.__execution_successful = True
        except sub.CalledProcessError as e:
            self.__stdout = e.stdout.decode('utf-8')
            self.__signal = e.returncode - 128

    def to_list(self):
        return [self.target,
                self.argument[:30] + (self.argument[30:] and '..') + ' (length:' + str(len(self.argument)) + ')',
                self.__num_to_sig(self.__signal),
                self.__stdout[:75] + (self.__stdout[75:] and '.. '), self.t]

    @staticmethod
    def __num_to_sig(sig):
        if sig > 0:
            return signal.Signals(sig).name
        elif sig == 0:
            return 'OK'
        else:
            return 'Unknown'

    def __repr__(self):
        return tabulate([self.to_list()])
