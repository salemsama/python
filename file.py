filePath = "Note.txt"

def append(note):
    with open(filePath,"a") as File:
        File.write(f"\n{note}")

def read():
    
    with open(filePath, 'r') as File:
        notes = File.readlines()
    return notes

with open(filePath,'w') as File:
    File.write(input("Enter your first note: "))

while True:
    choice = input("To write new note enter W, to read your notes R, else to exit: ")
    if choice.lower() == "w":
        append(input("Write your note: "))
    elif choice.lower() == "r":
        for note in read():
            print(note,end="")
        print("")
    else:
        break