import requests
import random
import sqlite3

url = "https://restcountries.com/v3.1/all"

response = requests.get(url)
countries = response.json()

conn = sqlite3.connect("countries.db")
cursor = conn.cursor()

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

conn.commit()
conn.close()
