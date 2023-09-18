import random             # Step 1 :import random module

def is_single_character(input_str):
    return len(input_str) == 1

def check_guess(guess, word):
    guess = guess.lower()  # Step 2: Convert the guess to lowercase

    if is_single_character(guess) and guess.isalpha():
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Guess a letter: ")

        if is_single_character(guess) and guess.isalpha():
            check_guess(guess, word)  # Step 3: Call check_guess function with 'word'
            
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Main code
word_list = ['orange', 'banana', 'carrot', 'pear', 'apple']
word = random.choice(word_list)


ask_for_input()  # Step 4: Call ask_for_input function
