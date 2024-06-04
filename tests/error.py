num = input("Enter a number: ")

try:
    print(int(num))
except ValueError :
    print("You didn't enter a number")