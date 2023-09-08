import random

def is_single_character(input_str):
    return len(input_str) == 1

word_list = ['orange', 'banana', 'carrot', 'pear', 'apple']
word = random.choice(word_list)
guess = input("Input a single character:")

if is_single_character(guess):
    print("The input is a single character.")
else:
    print("The input is not a single character.")
