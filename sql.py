import pypyodbc

driverName = "SQL Server"
serverName = "LAPTOP-IA935KR0\SQLEXPRESS"
databaseName = "test"

def main():
    try:
        connectionString = f"""
            DRIVER={{{driverName}}};
            SERVER={serverName};
            DATABASE={databaseName};
            Trusted_Connection=yes;
        """
        connection = pypyodbc.connect(connectionString, autocommit=True)
        db = connection.cursor()
        db.execute("select * from USERS")
        #db.execute("CREATE TABLE USERS( ID INT PRIMARY KEY, NAME VARCHAR(50), AGE INT, NATIONALITY VARCHAR(50))")
        
        print("Welcome!")
        while True:
            choice = input("for Input type i, for search s, for Edit e, for delete d, and x for exit\n").lower()
            match(choice):
                case "x":
                    break
                case "i":
                    inp(db)
                case "s":
                    search(db)
                case "e":
                    edit(db)
                case "d":
                    delete(db)

    except Exception as Error:
        print("Couldn't connect to database")
    finally:
        db.close()
        connection.close()


def inp(db):
    ID = input("ID: ")
    name = input("Name: ")
    age = input("Age: ")
    nation = input("Nationality: ")
    query = "INSERT INTO USERS (ID, NAME, AGE, NATIONALITY) VALUES(?, ?, ?, ?)"
    VALUES = (ID, name, age, nation)
    db.execute(query, VALUES)

def search(db):
    name = input("search for name: ")
    query = "SELECT * FROM USERS WHERE NAME = ?"
    values = (name,)
    db.execute(query, values)
    results = db.fetchall()
    for result in results:
        print (result)

def edit(db):
    oldName = input("name of edited user: ")
    query = "UPDATE USERS SET NAME = ? WHERE NAME = ?"
    newName = input("Enter the new name: ")
    values = (newName, oldName)
    db.execute(query, values)

def delete(db):
    name = input("delete user name: ")
    query = "DELETE FROM USERS WHERE NAME = ?"
    VALUES = (name,)
    db.execute(query, VALUES)
main()