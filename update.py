import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; '
                                r'DBQ=C:\Users\Rupido\Desktop\CPEN 60 Object Oriented Programming\Database1.accdb;')

    user_id = 11
    Fullname = 'Baby Angel E. Rupido'

    database = connection.cursor()
    database.execute('UPDATE Table1 set Fullname=? where id=?', (Fullname, user_id))
    connection.commit()
    print('Database is updated.')
except pyodbc.Error:
    print('Database is NOT connected.')