from random import randrange
import re

class invalidGuess(Exception):
    def __init__(self, error):
        self.error = error


class gameEnded(Exception):
    def __init__(self, won, word):
        self.won = won
        self.word = word


class HangmanGame:
    def __init__(self):
        self.previous_letters = []
        self.remaining_guesses = 5

        word = self.__generateWord()
        self.remaining_letters = word
        self.full_word = word
        self.display_word = re.sub('[a-zA-Z]', '_', self.full_word)

        print('Hangman')
        print('You have {} chances. Start guessing.'.format(self.remaining_guesses))
        print('Your word: ', " ".join(self.display_word), '\n')
        

    def __generateWord(self):
        with open('words.txt', 'r') as f:
            hangman_words = f.read().splitlines()

        random_num = randrange(len(hangman_words))
        word = hangman_words[random_num]    
        return word


    def __printStatus(self):
        print('{} remaining guesses'.format(self.remaining_guesses))
        print('Letters tried so far [%s]' % ', '.join(map(str, self.previous_letters)))
        print('Your word: ', " ".join(self.display_word), '\n')


    def playGame(self):
        while True:
            letter = input('Type Letter: ').lower()

            try:
                guessCorrect = self.__guessLetter(letter)

                if guessCorrect:
                    print(letter + ' was in the word. Continue!')
                    self.__printStatus()
                else:
                    print(letter + ' was not in the word') 
                    self.__printStatus()

            except invalidGuess as IG:
                print(IG.error + '\n')

            except gameEnded as GE:
                if GE.won:
                    print('Congratulations, you have won the game. Your word was: {}'.format(GE.word))
                else:
                    print('Your man died. The word was: {}'.format(GE.word))

                return GE.won
        

    def __guessLetter(self, letter):
        if len(letter) != 1:
            raise invalidGuess('Only Type one letter')
        elif letter.isalpha() == False:
            raise invalidGuess('Type in letters only')
        elif letter in self.previous_letters:
            raise invalidGuess('Already tried this letter!')

        self.previous_letters.append(letter)

        if letter in self.remaining_letters:
            # find position of character
            for position in range(len(self.full_word)):
                if letter == self.full_word[position]:
                    disp_list = list(self.display_word)
                    disp_list[position] = letter
                    self.display_word = "".join(disp_list)

            self.remaining_letters = self.remaining_letters.replace(letter, '')
            if self.remaining_letters == '':
                raise gameEnded(True, self.full_word)

            return True
        else:
            self.remaining_guesses = self.remaining_guesses - 1

            if self.remaining_guesses == 0:
                raise gameEnded(False, self.full_word)
                
            else:
                return False
