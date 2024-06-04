import random

rand =  random.randrange(1,6)

guessed = False
while not guessed:
    guess = input("Guess a number: ")
    if int(guess) == rand:
        guessed = True
        print("Won!!")
    else:
        print("wrong!! \nGuess again")