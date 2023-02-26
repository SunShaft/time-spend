import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='root',
                     database='TEST')

cursor = db.cursor()

# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,  
#          SEX CHAR(1),
#          INCOME FLOAT )"""
 
# cursor.execute(sql)

cursor.execute("show tables")

data = cursor.fetchone()

print(data)

db.close()