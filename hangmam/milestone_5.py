import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        '''
        Initialize the hangman game.

        '''
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

        print(f"The mystery word has {self.num_letters} characters")
        print(" ".join(self.word_guessed))

    def check_guess(self, guess):
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        '''
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")

            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess

            self.num_letters -= 1
        else:
            self.num_lives -= 1  # Step 2: Reduce num_lives by 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_guess method.

        '''
        while True:
            guess = input("Guess a letter: ")

            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

                if self.num_lives == 0:
                    print("You're out of lives! The word was:", self.word)
                    break
                elif self.num_letters == 0:
                    print("Congratulations! You guessed the word:", self.word)
                    break
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list,num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost !')
            break
        elif game.num_lives > 0:
            game.ask_for_input()
        else:
            print('Congratulations!.You won the game')
            break

if __name__ == "__main__":
    word_list = ['apple', 'banana', 'pear', 'orange', 'carrot']
    play_game(word_list)

