from datetime import date                   
import psycopg2
import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage
load_dotenv()
DB_PASSWORD = os.getenv('DB_PASSWORD')
my_email = os.getenv('EMAIL_USER')
app_password =os.getenv('EMAIL_PASS')

connection = psycopg2.connect(
user = 'postgres',
password = DB_PASSWORD,
host = 'localhost',
port = '5432',
database = 'dvdrental'
)

cursor = connection.cursor()
def birthday_wish(customer, customer_email):
    msg = EmailMessage()
    msg['subject'] = "Happy Birth from Nje firm"
    msg['from'] = my_email
    msg['to'] = customer_email
    msg.set_content(f"hey {customer} Wishing you a happy and a blessed birthday, Enjoy your day. we appreciate you being part of our success stories over the years")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(my_email, app_password)
            smtp.send_message(msg)
            return True
    except Exception as e :
        print(f"error sending the wish to {customer} {e}")
        return False
    


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
          name = person[0]
          email = person[1]
          if birthday_wish(name, email):
            print(f" success birthday message sent to {name} with {email} ")
          else:
              print(f" error birthday massage not sent to {name}")
    cursor.close()
    connection.close()


whose_birthday()