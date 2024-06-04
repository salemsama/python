import datetime

def stringToDate(date):
    year,month,day = date.split("/")
    return datetime.date(int(year), int(month), int(day))



firstName = input("First Name: ")
secondName = input("Second Name: ")
familyName = input("Family Name: ")

birthDate = stringToDate(input("Birth Date: "))

age = int(input("Age: "))

print("-"*10)
print("Full Name: ", firstName, secondName, familyName)
print("Birth date: ", birthDate.year, birthDate.month, birthDate.day)
print("Age: ",age)