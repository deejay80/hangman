import random

word_list  = ['orange','banana','carrot','pear','apple']
word = random.choice(word_list)
guess = input("Input a single character:")

if len(guess) == 1 and word.isalpha():
  print("Good guess!")
else:
 print("Oops!That is not a valid input")