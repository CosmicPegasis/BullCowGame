from settings import Settings


# Make a class BullCowGame
class BullCowGame:

    # Bring in word and other setting
    def __init__(self):
        self.settings = Settings()
        self.turns = self.settings.turns
        self.word_length = self.settings.word_length
        self.word = self.settings.word

    # Print introduction
    def intro(self):
        print('Hello! Welcome to the Bull Cow Game!')

    # Ask the question and record the input
    def question(self):
        self.input = input('Guess the ' + str(self.word_length)
                           + ' letter isogram: ')

    # Match the input with the answer

    # Display Bulls and Cows

    # Increment the number of turns

    #  Display whether the player won or lost

    # Main
    def main(self):
        self.intro()
        self.question()

game = BullCowGame()
game.main()