import pyodbc

cnxn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=DEVACCESSA-PC\LOGIDEV2016;'
                      'DATABASE=DATAKS_MC;'
                      'UID=sa;'
                      'PWD=Logi2131')
                      #'Trusted_Connection=yes;')

cursor = cnxn.cursor()
cursor.execute('select top (10) * FROM [DATAKS_MC].[dbo].[POS_TAB]')

for row in cursor:
    print(row)
    
cursor.close()
cnxn.close()
