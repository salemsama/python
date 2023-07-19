import random

rand =  random.randrange(1,6)

def guess(num,ran):
    if int(num) == ran:
        return True
    return False

print("Guess the number(1-5) 2 players version\nEvery player got 2 turns")

for i in range(2):
    player1 = input("Player1 turn: ")
    if guess(player1,rand):
        exit("Player1 won")
    
    player2 = input("Player2 turn: ")
    if guess(player2,rand):
        exit("Player2 won")

print("It's a draw")