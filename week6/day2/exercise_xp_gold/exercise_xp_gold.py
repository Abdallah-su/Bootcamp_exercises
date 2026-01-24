from datetime import date                   
import psycopg2
connection = psycopg2.connect(
user = 'postgres',
password = 'Abs0240574227',
host = 'localhost',
port = '5432',
database = 'menu'
)

cursor = connection.cursor()
def my_dictionary(username, user_password):
   #user_login ={'Avner Wolf': 'abcd1', 'Kofi Amoah':'efgh1', 'Kwaku Hustler': 'ijkl1' }
   
    query = "select username, password from user_login where username = %s and password = %s"
    cursor.execute(query, (username, user_password))
    connection.commit()
    user_detail = cursor.fetchone()
    return user_detail

def my_authentication():
    global log_in 
    global sign_up
    authenticate = False
    while True: 
     username = input ('input your name: ').title()
     user_password = input('input your password; ')
     authenticate = my_dictionary(username, user_password)
     if authenticate:
        print("login success")
        log_in = username
        break
     else :
        print("incorrect username or password, try again")
        user_sign_up =input("you can select S to sign up or E to exit").upper()
        if user_sign_up == 'S':
          username = input ('input your name: ').title()
          user_password = input('input your password; ') 
          if not authenticate:
             print('sign up sucess')  
             sign_up = username
             query = """insert into user_login(username, password)
             values (%s, %s)"""
             cursor.execute(query, (username, user_password))
             connection.commit()
             break
          else: print("sorry! incorrect username or username is not availabe")

def user_choice():
    user_choice = input('Select L to login or E to exit: ').upper()
    if user_choice == 'L': 
        my_authentication()
    else:
       exit()

user_choice()




