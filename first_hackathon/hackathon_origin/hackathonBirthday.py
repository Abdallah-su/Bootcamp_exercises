from datetime import date                   
import psycopg2
connection = psycopg2.connect(
user = 'postgres',
password = 'Abs0240574227',
host = 'localhost',
port = '5432',
database = 'dvdrental'
)

cursor = connection.cursor()

def whose_birthday():
    current_month = date.today().month
    current_day = date.today().day
    query = """select first_name, email from customer where
    extract(month from birth_date) = %s and
    extract(day from birth_date) = %s """
    cursor.execute(query,(current_month,current_day))
    celebrants = cursor.fetchall()
    if not celebrants:
        print(f" no birthday message for {date.today()}")
    else:
        print(f"found {len(celebrants)}birthday(s)!")
        for  person in celebrants:
          print(f"sending [automated] birthday message to {person[0]}({person[1]}) ")
    cursor.close()
    connection.close()

whose_birthday()