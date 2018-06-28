import itertools


class ArgumentGenerator:
    FUZZ_ALPHABET = ['%d', '%ld', '%f', '%c', '%c', '%s', '%p', '%x', '%j', '%n']

    def __init__(self, t, max_len=16337):
        self.t = t
        self.max_len = max_len

    def generator(self):
        if self.t == 'fstring':
            return self.__fuzz_generator()
        elif self.t == 'oflow':
            return self.__a_generator()

    def __fuzz_generator(self):
        for s in range(1, self.max_len + 1):
            for comb in itertools.combinations_with_replacement(ArgumentGenerator.FUZZ_ALPHABET, s):
                yield ''.join(comb)

    def __a_generator(self):
        for s in range(1, self.max_len + 1):
            yield s * 'A'


if __name__ == '__main__':
    pass
