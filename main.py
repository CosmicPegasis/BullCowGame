from settings import Settings


# Make a class BullCowGame
class BullCowGame:

    # Bring in word and other setting
    def __init__(self):
        self.settings = Settings()
        self.turns = self.settings.turns
        self.word_length = self.settings.word_length
        self.word = self.settings.word

        self.bulls = 0
        self.cows = 0

        self.turn = 1

        self.running_game = True

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
        
    # TODO AntiCheat

    # Game
    def play_game(self):
        for t in range(self.turns):
            print('\n')
            self.question()
            self.check_ans()
            self.answer_results()
            if self.bulls == self.word_length and self.turn <= self.turns:
                print('You Won!')
                break
            self.end_turn()

        else:
            print('Sorry, you lost.')
            self.running_game = False
    # Main
    def main(self):
        self.intro()
        self.play_game()

game = BullCowGame()
game.main()
