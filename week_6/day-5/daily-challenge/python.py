import requests
import random
# import sqlite3
import psycopg2


HOSTNAME = 'localhost'
USERNAME = 'guilbert'
PASSWORD = 'guilly'
DATABASE = 'restCountries'

url = "https://restcountries.com/v3.1/all"

response = requests.get(url)
countries = response.json()

postgres_db_connection = psycopg2.connect(
    host=HOSTNAME, 
    user=USERNAME, 
    password=PASSWORD, 
    dbname=DATABASE )

cursor = postgres_db_connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS countries (
                    name TEXT,
                    capital TEXT,
                    flag TEXT,
                    subregion TEXT,
                    population INTEGER
                )""")

for _ in range(10):
    country = random.choice(countries)
    name = country["name"]["common"]
    capital = country["capital"][0]
    flag = country["flags"]["png"]
    subregion = country["subregion"]
    population = country["population"]
    
    cursor.execute(name, capital, flag, subregion, population)

postgres_db_connection.commit()
postgres_db_connection.close()
