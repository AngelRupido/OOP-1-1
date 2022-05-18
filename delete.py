import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; '
                                r'DBQ=C:\Users\Rupido\Desktop\CPEN 60 Object Oriented Programming\Database1.accdb;')

    user_id = 9

    database = connection.cursor()
    database.execute('DELETE from Table1 where id=?', user_id)
    connection.commit()
    print("Record is deleted.")

except pyodbc.Error:
    print("Database is NOT connected.")