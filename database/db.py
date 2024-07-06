import pymysql
db_host = 'instance-cym.cjekikmkoq9h.us-east-2.rds.amazonaws.com'
db_user = 'dianah'
db_password = 'Hdez2024..'
db_database = 'db_cym'
db_table = 'MASCOTAS'

def connectionSQL():
    try:
        connectio_sql = pymysql.connect(
            host = db_host,
            user = db_user,
            password = db_password,
            database = db_database
        )
        print("Successfull connection to the database")
        return connectio_sql
    except:
        print("Error connecting to the database")
        return None

def add_user(nombreMascota, propietario, petType, raza, sexo, edad):
    intruction_sql = "INSERT INTO " + db_table + " (nombreMascota, propietario, tipoMascota, raza, sexo,edad) VALUES ('"+nombreMascota+"', '"+propietario+"', '"+petType+"', '"+raza+"', '"+sexo+"', "+edad+");"
    print(intruction_sql)
    connection_sql = connectionSQL()
    try:
        if connection_sql != None:
            cursor = connection_sql.cursor()
            cursor.execute(intruction_sql)
            connection_sql.commit()
        else:
            print("Error connecting to the database")
    except Exception as err:
        print(err)
