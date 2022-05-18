import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; '
                                r'DBQ=C:\Users\Rupido\Desktop\CPEN 60 Object Oriented Programming\Database1.accdb;')
    print("Database is Connected.")

except pyodbc.Error:
    print("Database is NOT connected.")