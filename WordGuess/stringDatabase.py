import random

class stringDatabase:
    temp_letters = []
    letters = []

    @classmethod
    def lettersToList(cls):
        '''
        This method will read all words from text file and store it into the list.
        '''
        with open('four_letters.txt') as files:
            for line in files:
                line = line.strip("\n")
                cls.temp_letters.append(line.split(" "))

        for list in cls.temp_letters:
            for word in list:
                cls.letters.append(word)

    @classmethod
    def word(cls):
        '''
        This method will select a random word from the list of words and return it.
        :return: It will return string with random word.
        '''
        return random.choice(cls.letters)
