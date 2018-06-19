class WordList:

    def __init__(self, word_list_path):
        self.word_list_path = word_list_path
        self.word_list = []
        self.__read_word_list()

    def __read_word_list(self):
        with open(self.word_list_path, 'r') as file:
            for line in file:
                if line:
                    l = line.strip()
                    if not l.startswith('#'):
                        self.word_list.append(l)
