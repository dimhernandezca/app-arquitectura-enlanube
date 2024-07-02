import pymysql
db_host = 'instance-cym.cjekikmkoq9h.us-east-2.rds.amazonaws.com'
db_user = 'dianah'
db_password = 'Hdez2024..'

def connectionSQL():
    try:
        connectio_sql = pymysql.connect(
            host = db_host,
            user = db_user,
            password = db_password
        )
        print("Successfull connection to the database")
    except:
        print("Error connecting to the database")