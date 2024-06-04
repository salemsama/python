from flask import Flask, render_template, request
import pypyodbc

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        
        Uname = request.form["username"]
        Upass = request.form["password"]
        result = checkDatabase(Uname,Upass)
        return result
    else:
        return "no data"
# connect to database and check username and password
def checkDatabase(Uname, Upass): 
    driverName = "SQL Server"
    serverName = "LAPTOP-IA935KR0\SQLEXPRESS"
    databaseName = "website"
    try:
        connectionString = f"""
            DRIVER={{{driverName}}};
            SERVER={serverName};
            DATABASE={databaseName};
            Trusted_Connection=yes;
        """
        connection = pypyodbc.connect(connectionString, autocommit=True)
        db = connection.cursor()

        query = f"select * from users where username = ?"
        values = (Uname,)
        db.execute(query, values)
        result = db.fetchall()
        if result:
            # if password is correct
            if result[0][2] == Upass:
                return "Logged in successfuly"
            else:
                return "wrong password"
        else:
            return "User not found"
            

    except Exception as Error:
        return "Error, couldn't connect to database."
    finally:
        db.close()
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)