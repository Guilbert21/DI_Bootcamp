import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'guilbert'
PASSWORD = 'guilly'
DATABASE = 'hr'

postgres_db_connection = psycopg2.connect(
    host=HOSTNAME, 
    user=USERNAME, 
    password=PASSWORD, 
    dbname=DATABASE )

cursor = postgres_db_connection.cursor()

query = "SELECT * FROM employees;"
cursor.execute(query)

results = cursor.fetchall()

print(results)

postgres_db_connection.close()

