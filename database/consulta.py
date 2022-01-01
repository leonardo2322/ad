import psycopg2 as pg
from db import conexion

try:
    with conexion.cursor() as cursor:
        query = """INSERT INTO Usuarios(usuario, passw) VALUES (%s,%s) """
        cursor.execute(query, name,passwor)
        conexion.commit()

except pg.Error as e:
    print("error de conexion",e)
finally:
    conexion.close()