class car:
    def __init__(self, model, year, HP) :
        self.model = model
        self.year = year
        self.HP = HP



class Ecar(car):
    def __init__(self, model, year, HP, battrySize):
        super().__init__(model, year, HP)
        self.battrySize = battrySize
    
    def range(self):
        return int(self.battrySize)*2



model = input("Enter the car model: ")
year = input("Year: ")
HP = input("Horse Power: ")
size = input("Battry Size: ")
myCar = Ecar(model, year, HP, size)

print(f"Your car range is: {myCar.range()}")