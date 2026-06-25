'''
Tâche 4: Les bases de données SQL, DBAPI
1. Créer une base de données, parcourir une table.
a) Créer une base de données
'''
import sqlite3 as dbapi2

conn = dbapi2.connect('test2.db')
cursor = conn.cursor()
cursor.execute("""
    create table VIN(
        NOM char(10),
        REGION char(10)
    )
""")
cursor.execute("create table BOUTEILLE(NOM char(10), ANNEE int)")
conn.commit()
cursor.execute("insert into VIN values ('Riesling','Alsace')")
cursor.execute("insert into VIN values ('Pommard','Bourgogne')")
cursor.execute("insert into BOUTEILLE (NOM,ANNEE) values ('Riesling',2005)")
conn.commit()
cursor.execute("SELECT * from VIN")
while True:
    row = cursor.fetchone()
    if row == None:
        break
    print(row[0], row[1])
cursor.close()