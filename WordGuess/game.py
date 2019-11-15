class game:
    '''
    This class maintains information and do different operations.
    '''
    dict = {"a": 8.17, "b": 1.49, "c": 2.78, "d": 4.25, "e": 12.70, "f": 2.23, "g": 2.02, "h": 6.09, "i": 6.97,
            "j": 0.15, "k": 0.77, "l": 4.03, "m": 2.41, "n": 6.75, "o": 7.51, "p": 1.93, "q": 0.10, "r": 5.99,
            "s": 6.33, "t": 9.06, "u": 2.76, "v": 0.98, "w": 2.36, "x": 0.15, "y": 1.97, "z": 0.07}
    score = 0
    game_number = 0
    status = ""
    bad_guesses = 0
    missed_letters = 0
    letter_request = 0
    data = [["Game", "Word", "Status", "Bad Guesses", "Missed Letters", "Score"]]

    def guessWord(self, current_word, current_guess):
        '''
        This method will ask word to guess and checks it matches with the actual word or not.
        :param current_word: It is string containing actual word.
        :param current_guess: It is string containing word with uncovered letters and covered letters.
        :return: It return True if strings matches and false if not.
        '''
        guessed_word = input("Enter your guess:  ")
        if current_word == guessed_word:
            game.countScore(current_word, current_guess)
            game.statusAssign("Success")
            game.countMissedLetters(current_word, current_guess)
            game.addList(current_word)
            return True
        else:
            game.countBadGuesses()
            return False

    def tellAnswer(self, current_word, current_guess):
        '''
        This method will return actual word if user is tired of guessing.
        :param current_word: It is string containing actual word.
        :param current_guess: It is string containing word with uncovered letters and covered letters.
        :return: It will return the string containing actual word.
        '''
        game.countMissedLetters(current_word, current_guess)
        game.statusAssign("Gave up")
        game.countScoreMinus(current_word)
        game.addList(current_word)
        return current_word

    def guessLetter(self, current_word, current_guess):
        '''
        This method will uncovers the guessed letters.
        :param current_word: It is string containing actual word.
        :param current_guess: It is string containing word with uncovered letters and covered letters.
        :return: It will return string with uncovered letters.
        '''
        guessed_letter = input("Enter a letter:  ")
        game.countLetterRequest()
        i = 0
        current_guess_list = list(current_guess)
        for letters in current_word:
            if guessed_letter == letters:
                current_guess_list[i] = guessed_letter
            i += 1

        current_guess = "".join(current_guess_list)
        if current_guess==current_word:
            game.countScore(current_word, current_guess)
            game.statusAssign("Success")
            game.countMissedLetters(current_word, current_guess)
            game.addList(current_word)
        return current_guess

    @classmethod
    def countScore(cls, current_word, current_guess):
        '''
        This method will count score for the user from uncovered letters.
        :param current_word: It is string containing actual word.
        :param current_guess: It is string containing word with uncovered letters and covered letters.
        '''
        for x, y in zip(current_word, current_guess):
            if x != y:
                cls.score += cls.dict[x]

    @classmethod
    def addList(cls, current_word):
        '''
        This method will store information after each round.
        :param current_word: It is string containing actual word.
        '''
        cls.game_number += 1
        if cls.letter_request != 0:
            cls.score = cls.score/cls.letter_request
        temp_score = cls.score/10
        cls.score = cls.score - (temp_score*cls.bad_guesses)
        temp_list = []
        temp_list.extend([cls.game_number, current_word, cls.status, cls.bad_guesses, cls.missed_letters, cls.score])
        cls.data.append(temp_list)
        game.resetAll()

    @classmethod
    def resetAll(cls):
        '''
        This method will reset all variables.
        '''
        cls.score = 0
        cls.status = ""
        cls.bad_guesses = 0
        cls.missed_letters = 0
        cls.letter_request = 0

    @classmethod
    def countLetterRequest(cls):
        '''
        This method will count number of letters requested to count score.
        '''
        cls.letter_request += 1

    @classmethod
    def countBadGuesses(cls):
        '''
        This method will count number of bad guesses to count score.
        '''
        cls.bad_guesses += 1

    @classmethod
    def statusAssign(cls, status_given):
        '''
        This method will assign status to display it in the end.
        :param status_given: It contains string success or give up.
        '''
        cls.status = status_given

    @classmethod
    def countMissedLetters(cls, current_word, current_guess):
        '''
        This method will count missed letters from a word for display purpose.
        :param current_word: It is string containing actual word.
        :param current_guess: It is string containing word with uncovered letters and covered letters.
        '''
        for x, y in zip(current_word, current_guess):
            if x != y:
                cls.missed_letters += 1

    @classmethod
    def countScoreMinus(cls, current_word):
        '''
        This method will count score in case of user gives up.
        :param current_word: It is string containing actual word.
        '''
        temp_score = 0
        for x in current_word:
            temp_score += cls.dict[x]
        cls.score = cls.score - temp_score

    @classmethod
    def printScore(cls):
        '''
        This method will print the score when user quit the game.
        '''
        final_score = 0
        for i in range(len(cls.data)):
            if i == 0:
                print("\n")
                print('{:<9s}{:<9s}{:<11s}{:<15s}{:<19s}{:<5s}'.format(cls.data[i][0], cls.data[i][1], cls.data[i][2], cls.data[i][3],
                                                                       cls.data[i][4], cls.data[i][5]))
                print('{:<9s}{:<9s}{:<11s}{:<15s}{:<19s}{:<5s}'.format("----", "----", "------", "-----------",
                                                                       "--------------", "-----"))
            else:
                print('{:<9d}{:<9s}{:<11s}{:<15d}{:<19d}{:<5.2f}'.format(cls.data[i][0], cls.data[i][1], cls.data[i][2], cls.data[i][3],
                                                                         cls.data[i][4], cls.data[i][5]))
                final_score += cls.data[i][5]

        print("\n")
        print("Final Score:  %.2f"% round(final_score, 2))