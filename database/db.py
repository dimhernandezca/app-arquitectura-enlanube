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
    except Exception as err:
        print("Error connecting to the database")
        print (err)
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
            print("User added")
            return True
        else:
            print("Error connecting to the database")
            return False 
    except Exception as err:
        print("Error creating the user")
        print(err)
        return False
        
def consult_user(nombreMascota, propietario):
        instruction_sql = "select * from MASCOTAS WHERE nombreMascota = '" + nombreMascota + "' AND propietario = '" + propietario + "';"
        connection_sql = connectionSQL()
        try:
            cursor = connection_sql.cursor()
            cursor.execute(instruction_sql)
            result_data = cursor.fetchall()
            print(result_data)
        except Exception as err:
            print("Error", err)