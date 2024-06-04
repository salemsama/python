

def main():
    name1 = input("Enter your name: ")
    age1 = input("Enter your age: ")
    phone1 = input("Enter your phone number: ")

    call(name = name1, age = age1, phone = phone1)


def call(**data):
    print(data)
    print(f"your name: {data['name']}\nyour age: {data['age']}\nyour Phone number: {data['phone']}")





if __name__=="__main__":
    main()