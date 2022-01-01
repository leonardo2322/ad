import psycopg2 as pg

try:
    credentials ={
        "dbname": "administracion",
        "user": "postgres",
        "password": "leonardo25537",
        "host": "localhost",
        "port": 5432
    }
    conexion = pg.connect(**credentials)
    print(conexion)
except pg.Error as e:
    print("ocurrio un error en la conexion", e)
