import psycopg2
import csv

param_connect = {
        "host": "localhost",
        "database": "north",
        "user": "postgres",
        "password": "5770"
    }

with psycopg2.connect(**param_connect) as conn:
    with conn.cursor() as cur:
        with open('north_data/customers_data.csv') as file:
            next(file)
            reader = csv.reader(file)
            for line in reader:
                cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", line)

            conn.commit()

        with open('north_data/employees_data.csv') as file:
            next(file)
            reader = csv.reader(file)
            for line in reader:
                cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", line)

            conn.commit()

        with open('north_data/orders_data.csv') as file:
            next(file)
            reader = csv.reader(file)
            for line in reader:
                cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", line)

            conn.commit()