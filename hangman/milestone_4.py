import random

#class definition
class Hangman:
#class constructor
    def __init__(self,word_list,num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self,guess):
        guess == guess.lower()

        if guess in self.word:
            print(f"Good guess!'{guess}' is in the word")
            
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess

            self.num_letters -= 1
        else:
            print('Sorry!,guess is not in word.Try again')

    def ask_for_input(self):
        while True:
            guess = input("try a guess: ")

            # check if guess is a single alphabetical letter
            if not guess.isalpha() or len(guess) != 1:
             print('Invalid letter.Please enter an alphabetical number')

            # check if guess is already in the list of guesses
            elif guess in self.list_of_guesses:
             print('You already tried that letter')

            else:
            # call the check_guess method and pass the guess
              self.check_guess(guess)
            # append guess to the list of guesses
              self.list_of_guesses.append(guess)
              if self.num_lives == 0:
                    print("You're out of lives! The word was:", self.word)
                    break
              elif self.num_letters == 0:
                    print("Congratulations! You guessed the word:", self.word)
                    break

if __name__ == "__main__":
    word_list = ['apple', 'banana', 'carrot', 'pear', 'orange']
    hangman_game = Hangman(word_list)
    hangman_game.ask_for_input() # call the ask_for_input method to test
            


