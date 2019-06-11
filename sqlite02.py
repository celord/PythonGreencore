import sqlite3


conexion=sqlite3.connect("bd1.db")
conexion.execute("insert into articulos(description,precio) values (?,?)", ("naranjas",23.50))
conexion.execute("insert into articulos(description,precio) values (?,?)", ("peras",34))
conexion.execute("insert into articulos(description,precio) values (?,?)", ("bananas",25))
conexion.commit()
conexion.close()