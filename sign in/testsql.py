import pypyodbc

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
    values = ("ahmed",)
    db.execute(query, values)
    result = db.fetchall()
    if result:
        print(result)
    else:
        print("none")
    
        

except Exception as Error:
    print("error")
finally:
    db.close()
    connection.close()