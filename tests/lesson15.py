numbers = []

x = input("how many number do you want to save? ")

for n in range(int(x)):
    numbers.append(input(f"enter number {n+1}: "))


print(numbers)