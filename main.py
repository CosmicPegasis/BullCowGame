"""This is called the BullCowGame. This is a simple
word guessing game. In this you have to guess the word which is
of given letters.
Bulls means the number of letters which are in the word and in correct place
Cows means the number of letter which are in the word but not
in the correct place

All settings such as number of turns, the word etc. can be changed from
settings.py"""

from settings import Settings


# Make a class BullCowGame
class BullCowGame:

    # Bring in word and other setting
    def __init__(self):
        self.settings = Settings()
        self.turns = self.settings.turns
        self.word_length = self.settings.word_length
        self.word = self.settings.word
        self.isogram = True

        self.bulls = 0
        self.cows = 0

        self.turn = 1

        self.running_game = True
        self.cheating = False

    # Print introduction
    def intro(self):
        print('Hello! Welcome to the Bull Cow Game!')

    # Ask the question and record the input
    def question(self):
        print('Try:', self.turn)
        self.input = input('Guess the ' + str(self.word_length)
                           + ' letter isogram: ')

    # Match the input with the answer
    def check_ans(self):

        # Match every letter in answer with every letter in word
        for a_letter in self.input:
            for w_letter in self.word:
                if a_letter == w_letter and \
                   self.input.index(a_letter) == self.word.index(w_letter):
                    self.bulls += 1

                elif a_letter == w_letter:
                    self.cows += 1

    # Display Bulls and Cows
    def answer_results(self):
        print('Bulls:', self.bulls)
        print('Cows:', self.cows)

    # End of turn maintenance
    def end_turn(self):
        self.turn += 1
        self.bulls = 0
        self.cows = 0

    def win_or_lose(self):
        if self.bulls == self.word_length and self.turn <= self.turns:
            print('You Won!')
            return self.turns + 1

    # Check if it's an isogram
    def check_isogram(self):
        for letter in self.input:
            repetition = 0
            for a in self.input:
                if letter == a:
                    repetition += 1

                if repetition > 1:
                    self.isogram = False

    # AntiCheat
    def anticheat(self):
        if len(self.input) != self.word_length:
            self.cheating = True

    # Game
    def play_game(self):
        t = 0
        while t in range(self.turns):
            print('\n')
            self.question()
            self.anticheat()
            self.check_isogram()
            if self.cheating is False:
                if self.isogram is True:
                    self.check_ans()
                    self.answer_results()
                    if self.bulls == self.word_length \
                            and self.turn <= self.turns:
                        print('You Won!')
                        break
                    self.end_turn()
                    t += 1
                else:
                    print('Sorry, your answer is not an isogram')
            else:
                print('Sorry, your answer isn\'t of',
                      self.word_length, 'letters')

        else:
            print('Sorry, you lost.')

    # Play Again
    def play_again(self):
        response = input('Want to play again?(y/n)')
        if response.lower() == 'n':
            self.running_game = False

        else:
            print('\n')
            self.turn = 1

    # Main
    def main(self):
        while self.running_game is True:
            self.intro()
            self.play_game()
            self.play_again()


game = BullCowGame()
game.main()
