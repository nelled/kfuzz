import subprocess as sub


class Executor:

    def __init__(self, target, argument):
        self.target = target
        self.argument = argument
        self.execution_successful = False
        self.stdout = ''
        self.signal = -1
        self.__execute()

    def __execute(self):
        try:
            output = sub.run(args=self.target + " " + self.argument, stdout=sub.PIPE, stderr=sub.STDOUT, shell=True, check=True)
            self.stdout = output.stdout.decode('utf-8')
            self.signal = output.returncode
            self.execution_successful = True
        except sub.CalledProcessError as e:
            self.stdout = e.stdout.decode('utf-8')
            self.signal = e.returncode - 128

    def to_list(self):
        return [self.target, self.argument[:75] + (self.argument[75:] and '..'), str(self.signal), self.stdout]

    def __repr__(self):
        return ":::".join(self.to_list())
