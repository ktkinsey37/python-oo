"""Word Finder: finds random words from a dictionary.

    >>> wf = WordFinder("test.txt")
    3 words read

    >>> wf = SpecialWordFinder("test.txt")
    1 words read

    >>> wf.random()
    'kale'
"""
import random

class WordFinder:

    def __init__(self, filename):
        self.filename = filename
        self.words_list = []
        self.file = open(self.filename, "r")
        self.read_file()
        print(f"{len(self.words_list)}" + " words read")

    def read_file(self):
        for line in self.file:
            self.words_list.append(line.rstrip("\n"))
        return len(self.words_list)

    def random(self):
        return random.choice(self.words_list)
            

    # can't figure out how to accept the file path as arg

class SpecialWordFinder(WordFinder):
    def __init__(self, filename):
        super().__init__(filename)

    def read_file(self):
        for line in self.file:
            if line.startswith("#") == False and line.startswith("\n") == False:
                self.words_list.append(line.rstrip("\n"))